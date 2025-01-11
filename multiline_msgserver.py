import socket

HOST = '0.0.0.0'
PORT = 12345

MAX_RECV = 20

def handle_client(client):
    while True:
        msg = ''
        size_str = client.recv(8).decode()
        assert(len(size_str) == 8)

        size = int(size_str)

        while len(msg) < size:
            chunk = client.recv(size - len(msg)).decode()
            if not chunk:
                print("Client disconnected")
                return
            msg += chunk

        print("Next client message is:")
        print(msg)

def start_server():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connected to client: {address}")
        handle_client(client_socket)

if __name__ == '__main__':
    start_server()