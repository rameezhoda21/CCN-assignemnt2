import socket
import time

HOST = '127.0.0.1'
PORT = 65433

total_time = 0
message_size = 0
received_count = 0
timeout_duration = 0.5  # seconds

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(timeout_duration)

    for i in range(100):
        message = f"Message {i}".encode()
        message_size += len(message)
        start_time = time.time()
        s.sendto(message, (HOST, PORT))

        try:
            data, _ = s.recvfrom(1024)
            end_time = time.time()
            round_trip_time = (end_time - start_time) * 1000
            total_time += round_trip_time
            received_count += 1
            print(f"Round-trip {i}: {round_trip_time:.2f} ms")
        except socket.timeout:
            print(f"Round-trip {i}: timed out (packet lost)")

# Final calculations
packet_loss_rate = (100 - received_count) / 100 * 100
average_latency = total_time / received_count if received_count else 0
throughput = message_size / (total_time / 1000) if total_time else 0

print(f"\nReceived: {received_count}/100")
print(f"Packet Loss Rate: {packet_loss_rate:.2f}%")
print(f"Average Latency: {average_latency:.2f} ms")
print(f"Throughput: {throughput:.2f} bytes/sec")
