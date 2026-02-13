from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class IPInfoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get client IP address
        client_ip = self.client_address[0]
        
        # Prepare response
        response = {
            "ip_address": client_ip,
            "port": self.client_address[1],
            "method": self.command,
            "path": self.path
        }
        
        # Send response
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), IPInfoHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()