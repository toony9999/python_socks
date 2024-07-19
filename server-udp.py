import socket

def start_udp_server(host='127.0.0.1', port=8888):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP server listening on {host}:{port}")
    
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")
        # Optionally, send a response
        server_socket.sendto(b"Message received", addr)

if __name__ == "__main__":
    start_udp_server()
