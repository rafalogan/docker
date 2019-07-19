import logging
import http.server
import socketserver
import getpass

class MyHTTPHandler(help.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - - [$s]%s\n"% (
            self.client_address[0],
            self.log_date_time_string(),
            format%args
        ))

logging.basicConfig(
    filename='/log/http-server.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info('inicializando...')
PROT = 8000

httpd = socketserver.TCPServer(("", PROT), MyHTTPHandler)
logging.info(' escutando a popota: %s', PROT)
logging.info('usuário: %s'. .getpass.getuser())
httpd.serve_forever()