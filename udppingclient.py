
import time
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSocket.settimeout(1)

server_addr = ("127.0.0.1", 12000)

for i in range(10):
    try:
        start = time.time()
        request = f"Ping {i} {start}".encode()
        clientSocket.sendto(request, server_addr)
        response = clientSocket.recv(1024)
        rtt = time.time() - start
        print(f"Message: {response.decode()}")
        print(f"RTT: {rtt} s\n")
    except socket.timeout:
        print("Request timed out\n")

clientSocket.close()