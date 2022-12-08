
# to handle connections
import socket
from _thread import start_new_thread
import sys

server = "172.25.190.192"
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


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0])+","+str(tup[1])

# starting position of players
pos = [(0, 0), (100, 100)]
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player%2])))
    reply = ""
    while True:
        # receive data from the client
        try:
            data = read_pos(conn.recv(2048).decode())
            # encode the information sending back to the client
            pos[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print(f'Received: {data}')
                print(f'Sending: {reply}')
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("Connection lost")
    conn.close()


currentPlayer = 0
# continuously look for connection
while True:
    # accept any incoming connection
    print("accepting connection...")
    conn, addr = s.accept()
    print(f'Connected to: {addr}')

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1