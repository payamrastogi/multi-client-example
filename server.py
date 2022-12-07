
# to handle connections
import socket
from _thread import start_new_thread
import sys

server = "10.2.42.78"
port = 5555

# setup socket
# connecting to IPV4 address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind server and port to socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# listening to the connection
# allow for unlimited connection if left blank
s.listen(2)
print("Waiting for connection, Server started")

def threaded_client(conn):
    reply = ""
    while True:
        # receive data from the client
        try:
            data = conn.recv(2048)
            # encode the information sending back to the client
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print(f'Received: {reply}')
                print(f'Sending: {reply}')
            conn.sendall(str.encode(reply))
        except:
            break;

# continuously look for connection
while True:
    # accept any incoming connection
    conn, addr = s.accept()
    print(f'Connected to: {addr}')

    start_new_thread(threaded_client, (conn, ))