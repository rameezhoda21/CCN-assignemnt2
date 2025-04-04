import socket
import time

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        for _ in range(100):
            start_time = time.time()
            data = conn.recv(1024)
            if not data:
                break
            response = b"Received: " + data
            conn.sendall(response)
            end_time = time.time()
            print(f"Processed message in {(end_time - start_time) * 1000:.2f} ms")
