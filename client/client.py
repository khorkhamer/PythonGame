import time
from server import Server

IP = "localhost"
PORT = 8889
MPORT = 8887


class Client(Server):


    def handle(self, message):
        return str(message) == "b'yes'"


    def move(self):
        self.send(IP, PORT, "move")
        while True:
            time.sleep(1)
            if self.queue.exists():
                if self.handle(self.queue.get()):
                    break
                else:
                    self.send(IP, PORT, "move")


    def turnArrow(self):
        self.send(IP, PORT, "turn")
        while True:
            time.sleep(1)
            if self.queue.exists():
                if self.handle(self.queue.get()):
                    break
                else:
                    self.send(IP, PORT, "turn")

    def start(self):
        self.start_server()

    def stop(self):
        self.send(IP, PORT, "end")
        self.stop_server()








g = Client(IP, MPORT)
g.start()


def move():
    g.move()

def turn():
    g.turnArrow()

def stop():
    g.stop()
