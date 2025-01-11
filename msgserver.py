import socket

HOST = '0.0.0.0'
PORT = 12345

MAX_RECV = 20

def handle_client(client):
    try:
        buffer = ''
        while True:
            msg = client.recv(MAX_RECV).decode()
            buffer += msg
    except Exception as e:
            print('Client done sending')
    print("Client message is:")
    print(buffer)

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
