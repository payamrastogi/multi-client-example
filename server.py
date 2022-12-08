
# to handle connections
import socket
from _thread import start_new_thread
from player import Player
import pickle

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

# starting position of players
players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player%2]))
    reply = ""
    while True:
        # receive data from the client
        try:
            data = pickle.loads(conn.recv(2048))
            # encode the information sending back to the client
            players[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print(f'Received: {data}')
                print(f'Sending: {reply}')
            conn.sendall(pickle.dumps(reply))
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