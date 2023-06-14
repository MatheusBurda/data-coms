import socket

PORT = 17171    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    print("Awaiting connection...")

    server_socket.bind(('', PORT))
    server_socket.listen()
    conn, addr = server_socket.accept()

    with conn:
        print(f"Connected to client on {addr}")

        while True:
            data = conn.recv(1024).decode('utf-8')
            
            if not data:
                break

            return_msg = f"Server Received: {data}"
            print(return_msg)
            conn.sendall(return_msg.encode('utf-8'))