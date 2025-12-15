#!/usr/bin/env python3
"""
Simple HTTP server with no-cache headers for localhost development
Run: python3 server.py
Then visit: http://localhost:8000
"""

import http.server
import socketserver
import os

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add no-cache headers
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Last-Modified', 'Thu, 01 Jan 1970 00:00:00 GMT')
        self.send_header('ETag', '')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

PORT = 8000

with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
    print("=" * 70)
    print(f"Server running at http://localhost:{PORT}")
    print("=" * 70)
    print("This server sends NO-CACHE headers to prevent browser caching")
    print("Press Ctrl+C to stop the server")
    print("=" * 70)
    httpd.serve_forever()
