import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("10.5.124.47", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever() #this works, but only on my own machine