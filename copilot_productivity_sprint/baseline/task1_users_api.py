import json
import re
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

users_db = {}

class UserRegistrationHandler(BaseHTTPRequestHandler):
    def send_response_json(self, status_code, payload):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode('utf-8'))

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path != '/users':
            self.send_response_json(404, {"error": "Not found"})
            return

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            body = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_response_json(400, {"error": "Invalid JSON"})
            return

        name = body.get('name', '')
        email = body.get('email', '')

        # Basic text and existence validation
        if not name or not isinstance(name, str) or not name.strip():
            self.send_response_json(400, {"error": "Missing or empty name"})
            return

        # Simple email regex for requirement
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.send_response_json(400, {"error": "Invalid email format"})
            return

        # Check for duplicates inside in-memory dictionary
        for user in users_db.values():
            if user['email'] == email:
                self.send_response_json(409, {"error": "Email already exists"})
                return

        user_id = str(uuid.uuid4())
        new_user = {
            "id": user_id,
            "name": name.strip(),
            "email": email.strip()
        }
        
        users_db[user_id] = new_user
        self.send_response_json(201, new_user)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, UserRegistrationHandler)
    print('Starting baseline server on port 8000...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
