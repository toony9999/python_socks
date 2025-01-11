import socket

HOST = 'localhost'
PORT = 12345

def get_user_message():
    msg = ''
    print("Enter multi-line message. Ctrl+C to finish:")
    while True:
        try:
            msg += input() + '\n'
        except KeyboardInterrupt as e:
            return msg
            
def send_message():
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))

    while True:
        msg = get_user_message()
        size = '%08d' % len(msg)        
        print("Message size: " + size)
        client_socket.send(('%08d' % len(msg)).encode())
        client_socket.send(msg.encode())
    
if __name__ == '__main__':
    send_message()