import socket
import time

HOST = '127.0.0.1'
PORT = 65432

total_time = 0
message_size = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(100):
        message = f"Message {i}".encode()
        message_size += len(message)
        start_time = time.time()
        s.sendall(message)
        data = s.recv(1024)
        end_time = time.time()
        round_trip_time = (end_time - start_time) * 1000
        total_time += round_trip_time
        print(f"Round-trip {i}: {round_trip_time:.2f} ms")

average_latency = total_time / 100
throughput = message_size / (total_time / 1000)  # bytes per second

print(f"\nAverage latency: {average_latency:.2f} ms")
print(f"Throughput: {throughput:.2f} bytes/sec")
