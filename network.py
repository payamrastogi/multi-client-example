import socket
# serialize objects
import pickle
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.25.190.192"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        # should print connected
        # print(self.id)

    def getP(self):
        return self.p

    def connect(self):
        try:
            print("Connecting...")
            self.client.connect(self.addr)
            print("Connected")
            # immediately send something
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

# n = Network()
# print(n.send("Hello"))
# print(n.send("Working"))