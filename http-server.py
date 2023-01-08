import http.server as http
import socketserver
from urllib.error import HTTPError
import urllib

port = 80
adress = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adress, handler, bind_and_activate=False)
httpd.allow_reuse_address = True
httpd.server_bind()
httpd.server_activate()

print("Server is started in the PORT {}".format(port))
print("Go in your navigator and go to this link : localhost:{}/".format(port))

httpd.serve_forever()
