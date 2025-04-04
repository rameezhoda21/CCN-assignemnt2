# how to run the files
open the files in VS code and run each python file in a dedicated terminal. Make sure to run the server files before the client files

# expected outputs
TCP_client output:
Average latency: 0.12 ms
Throughput: 84884.11 bytes/sec

UDP_client output:
Received: 84/100
Packet Loss Rate: 16.00%
Average Latency: 1.81 ms
Throughput: 6499.45 bytes/sec

# comparison analysis
TCP has higher round-trip time (RTT) due to connection setup, acknowledgments, and retransmissions, while UDP offers lower latency by skipping these steps, making it faster for time-sensitive communication. UDP does not guarantee delivery or order—lost packets are simply ignored—whereas TCP ensures reliable and ordered delivery using sequence numbers, acknowledgments, and retransmissions. For throughput, TCP is better suited for large, reliable data transfers but introduces overhead due to error checking and congestion control; UDP, on the other hand, is faster for short bursts or real-time data because of its minimal overhead. Applications should use TCP when data integrity and order are critical, such as in web browsing (HTTP/HTTPS), file transfers (FTP), emails (SMTP), and remote access (SSH). UDP is ideal for scenarios where speed is more important than perfect reliability, such as VoIP (Zoom, Skype), online gaming, video streaming, and DNS queries.

# how have i accomplished this


# test log files
