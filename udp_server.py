import socket
import random

HOST = '127.0.0.1'
PORT = 65433
LOSS_PROBABILITY = 0.2  # 20% chance to ignore packet

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)
        message = data.decode()

        # Simulate packet loss
        if random.random() < LOSS_PROBABILITY:
            print(f"Dropped packet: {message}")
            continue

        print(f"Received: {message} from {addr}")
        response = f"Received: {message}".encode()
        s.sendto(response, addr)
