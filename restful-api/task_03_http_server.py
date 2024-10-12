#!/usr/bin/python3

import http.server
import socketserver
import json
# esto empieza el server en el port especificado
PORT = 8000


# esto es un subclass de http.server.BaseHTTPRequestHandler
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":

            # estableciendo response code a 200
            self.send_response(200)

            # esto establece content-type a applicacion/json
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # creando la data json
            data = {"name": "John", "age": 30, "city": "New York"}

            # escribribiendo el json response
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not found")


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
