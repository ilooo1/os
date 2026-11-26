import http.server, socketserver
print("GUI запущен: http://localhost:8081/gui.html")
socketserver.TCPServer(("", 8081), http.server.SimpleHTTPRequestHandler).serve_forever()
