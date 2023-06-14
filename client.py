
import socket
from time import sleep

HOST = "192.168.0.8"    # The server's hostname or IP address
PORT = 17171            # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to server on {HOST}")

    message = input('Message: ')

    while message != '':
        s.sendall(message.encode('utf-8'))
        
        data = s.recv(1024).decode('utf-8')

        print(f"Client: {data}")
        message = input('Message: ')


    print(f"Closing connection to {HOST}.")
    s.close()