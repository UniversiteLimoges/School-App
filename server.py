#!/usr/bin/python3
import http.server

PORT = 8888
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/web"]

try:
    print("Serveur actif sur le port :", PORT)
    httpd = server(server_address, handler)
    httpd.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.close()