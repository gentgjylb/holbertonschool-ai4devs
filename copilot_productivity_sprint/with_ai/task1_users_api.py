import json
import re
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

users_db = {}

class UserAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, status, data):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        # Path extraction
        if urlparse(self.path).path != '/users':
            return self._send_json(404, {"error": "Not Found"})

        # Load safely
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
        except (ValueError, TypeError):
            return self._send_json(400, {"error": "Invalid payload"})

        name = body.get('name', '').strip() if isinstance(body.get('name'), str) else ''
        email = body.get('email', '').strip() if isinstance(body.get('email'), str) else ''

        if not name:
            return self._send_json(400, {"error": "Missing name"})
        
        # Regex format verify
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            return self._send_json(400, {"error": "Invalid email format"})

        # O(N) duplicate email uniqueness checker
        if any(u['email'] == email for u in users_db.values()):
            return self._send_json(409, {"error": "Email already exists"})

        # Assignment
        user_id = str(uuid.uuid4())
        users_db[user_id] = {"id": user_id, "name": name, "email": email}
        self._send_json(201, users_db[user_id])

if __name__ == '__main__':
    print('AI server live on 8000...')
    HTTPServer(('', 8000), UserAPIHandler).serve_forever()
