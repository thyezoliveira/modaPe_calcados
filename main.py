from http.server import HTTPServer, BaseHTTPRequestHandler

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Olá modaPé Calçados!'.encode())

def main():
    PORT = 8000
    server_adress = ('localhost', PORT)
    server = HTTPServer(server_adress, echoHandler)
    print('Server running on port %s.' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()