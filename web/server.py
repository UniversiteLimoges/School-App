#!/usr/bin/python3
import http.server

PORT = 8888
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

class myHandler(handler):

	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send the html message
		self.wfile.write("Hello World !")
		return

try:
    print("Serveur actif sur le port :", PORT)
    httpd = server(server_address, handler)
    httpd.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.close()