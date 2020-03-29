import socket
from server import HOSTNAME, PORT


if __name__ == '__main__':

    with socket.socket() as sock:
        # или sock = socket.socket(), но после всего не забудьте закрыть сокет sock.close()

        sock.connect((HOSTNAME, PORT))

        sock.sendall(f'{input("Enter text: ")}\n'.encode())

        data = sock.recv(1024)

        print(f'received: {data.decode()}')