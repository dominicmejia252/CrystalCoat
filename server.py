#!/usr/bin/env python3
import http.server
import os

class CrystalCoatHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path.startswith('/CrystalCoat'):
            path = path[len('/CrystalCoat'):]
        if not path:
            path = '/'
        return super().translate_path(path)

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.HTTPServer(('0.0.0.0', 5000), CrystalCoatHandler)
    print('Serving on http://0.0.0.0:5000')
    server.serve_forever()
