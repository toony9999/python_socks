import socket

def start_udp_client(host='127.0.0.1', port=8888):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto("Hello from the client\n".encode(), (host, port))
    
    # Optionally, receive a response
    data, addr = client_socket.recvfrom(1024)
    print(f"Received response from {addr}: {data.decode()}")

if __name__ == "__main__":
    start_udp_client()
