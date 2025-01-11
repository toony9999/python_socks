import socket

HOST = 'localhost'
PORT = 12345

def send_message():
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))

    print("Enter your message:")
    line = input()
    
    client_socket.send(line.encode())
    
if __name__ == '__main__':
    send_message()