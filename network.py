import socket
import pickle

# 172.87.175.81


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.150"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()  # tells what player you are

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        # sends what to do, receives state of game as response and returns it
        # to client
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

    def getP(self):
        return self.p
