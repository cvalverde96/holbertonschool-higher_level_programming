import http.server
import socketserver
import json

"""
el modulo http.server se utiliza para hacer request de http
contiene la clase BaseHTTPRequestHandler
el modulo socketserver se utiliza para crear servidores
el modulo json se utiliza para convertir dict python en JSON string
"""


# estamos haciendo una subclase de BaseHTTPRequestHandler, para los requests
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # este metodo se trigger cada vez que un GET request es recibido
    def do_GET(self):

        # atributo para validar si el reqeusted path es /root
        if self.path == "/":

            # para enviar status code ok
            self.send_response(200)

            # estos metodos son para enviar los headers, en text plain
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # enviando el mensaje como bytes utilizando wfile
            self.wfile.write(b"Hello, this is a simple API!")

        # atributo para validar si el reqeusted path es /data
        elif self.path == "/data":

            # dict python que vamos a retornar como un json string
            response_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            # para enviar status code ok
            self.send_response(200)

            # estos metodos son para enviar los headers, en formato json
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # convierte el python dict an un json string y encodes
            self.wfile.write(json.dumps(response_data).encode("utf-8"))

        # atributo para validar si el reqeusted path es /info
        elif self.path == "/info":

            # dict python que vamos a retornar como un json string
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            # para enviar status code ok
            self.send_response(200)

            # estos metodos son para enviar los headers, en formato json
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # convierte el python dict an un json string y encodes
            self.wfile.write(json.dumps(info_data).encode("utf-8"))

        # atributo para validar si el reqeusted path es /status
        elif self.path == "/status":

            # para enviar status code ok
            self.send_response(200)

            # estos metodos son para enviar los headers, en text plain
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # queso
            self.wfile.write(b"OK")

        # luego de validar todos los ifs, si no reconocemos endpoint, 404 error
        else:
            self.send_error(404, "Endpoint not found")


# variable para declarar en que port vamos a estar escuchando
PORT = 8000


# creando un tcp server  para escuchar en el port designado
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}...")
    # mantiene el server corriendo hasta ser interrumpido
    httpd.serve_forever()
