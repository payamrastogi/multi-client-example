import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.25.190.192"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        # should print connected
        # print(self.id)

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            print("Connecting...")
            self.client.connect(self.addr)
            print("Connected")
            # immediately send something
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

# n = Network()
# print(n.send("Hello"))
# print(n.send("Working"))