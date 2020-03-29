import socket

HOSTNAME = 'localhost'
PORT = 8182


if __name__ == '__main__':

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        # сетевой TCP сокет

        server_sock.bind((HOSTNAME, PORT))  # занимаем PORT на интерфейсе, соответствующем HOSTNAME
        server_sock.listen(1)  # запускаем режим прослушивания

        print(f'listening on {HOSTNAME}:{PORT}')

        conn, addr = server_sock.accept()  # ожидаем подключения
        print(f'connected: {addr}')

        data = conn.recv(1024)
        print(f'received message: {data.decode()}')

        conn.send(data.upper())
        conn.close()
