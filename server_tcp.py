import socket

def start_server(host='127.0.0.1', port=8080):
    # Create a TCP socket
    server_socket = socket.socket()
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    # Accept a connection
    con, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    # Receive data from the client
    data = con.recv(1024)
    print(f"Received message: {data.decode()}")
    
    # Send a response back to the client
    con.sendall("Message received".encode())

if __name__ == "__main__":
    start_server()
