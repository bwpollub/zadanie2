import http.server
import socketserver
import datetime
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO) # konfiguracja logowania

PORT = 8080 # Port do nasluchiwania polaczen

# klasa do obslugi zapytan HTTP

class HttpServerRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        ip_address = self.client_address[0] # pobranie ip klienta

        # wyswietlenie adresu ip klienta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>IP klienta</title></head>', 'utf-8'))
        self.wfile.write(bytes(f'<body><p>IP klienta: {ip_address}</p>', 'utf-8'))

        # wyswietlenie aktualnej daty i czasu
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        self.wfile.write(bytes(f'<p>Aktualna data i czas: {timestamp}</p>', 'utf-8'))
        self.wfile.write(bytes('</body></html>', 'utf-8'))

# uruchomienie serwera http
with socketserver.TCPServer(('', PORT), HttpServerRequestHandler) as http_server:
    logging.info('Serwer uruchomiony')
    logging.info('Autor: Bartłomiej Wójtowicz')
    logging.info(f'Port: {PORT}')

    # wlaczenie nasluchiwania
    http_server.serve_forever()
