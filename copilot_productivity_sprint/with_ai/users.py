import json
import re
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

users_db = {}

class UserAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, status, dict_resp):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(dict_resp).encode('utf-8'))

    def do_POST(self):
        if urlparse(self.path).path != '/users':
            return self._send_json(404, {"error": "Not Found"})

        try:
            content_length = int(self.headers.get('Content-Length', 0))
            payload = json.loads(self.rfile.read(content_length))
        except (ValueError, TypeError):
            return self._send_json(400, {"error": "Invalid JSON Payload"})

        name = payload.get('name', '').strip() if isinstance(payload.get('name'), str) else ''
        email = payload.get('email', '').strip() if isinstance(payload.get('email'), str) else ''

        if not name:
            return self._send_json(400, {"error": "Name field missing or empty"})
        
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, email):
            return self._send_json(400, {"error": "Invalid email formatting structure"})

        if any(usr['email'] == email for usr in users_db.values()):
            return self._send_json(409, {"error": "Email address already registered"})

        unique_id = str(uuid.uuid4())
        users_db[unique_id] = {"id": unique_id, "name": name, "email": email}
        self._send_json(201, users_db[unique_id])

if __name__ == '__main__':
    HTTPServer(('', 8000), UserAPIHandler).serve_forever()
