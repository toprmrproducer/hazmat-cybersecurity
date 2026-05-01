#!/usr/bin/env python3
"""Simple HTTP server that forces no-cache on every response."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

with ThreadingHTTPServer(('0.0.0.0', PORT), NoCacheHandler) as httpd:
    print(f"Serving with no-cache on http://localhost:{PORT}")
    httpd.serve_forever()
