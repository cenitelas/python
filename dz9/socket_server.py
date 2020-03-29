import socketserver
from server import HOSTNAME, PORT
import xmltodict, json ,dicttoxml

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        print(f'connection received: {self.client_address}')
        data = self.rfile.readline().strip()
        try:
                text = xmltodict.parse(data.decode())
                result = json.dumps(text).encode('utf-8')
                self.wfile.write(result)
        except Exception as e:
            try:
                text = json.loads(data.decode())
                result = dicttoxml.dicttoxml(text)
                self.wfile.write(result)
            except Exception as e:
                self.wfile.write('error parse\n'.encode())




if __name__ == "__main__":

    with socketserver.TCPServer((HOSTNAME, PORT), MyTCPHandler) as server:
        server.serve_forever()