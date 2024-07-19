import socket

def start_client(host='127.0.0.1', port=8080):
    # Create a TCP socket
    client_socket = socket.socket()
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send a message to the server
    message = "Hello from the client side!"
    client_socket.sendall(message.encode())
    
    # Receive a response from the server
    response = client_socket.recv(1024)
    print(f"Received from server: {response.decode()}")

if __name__ == "__main__":
    start_client()
