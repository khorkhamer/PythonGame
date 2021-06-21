from server import Server
from Constants import *


class Controller(Server):

    def handle(self, message):
        pass

    def handle(self, message, scene):
        if scene.get_state() == "Animating":
            self.send(IP, PORT, "no")
        elif scene.get_state() == "Idle":
            if str(message) == "b'move'":
                self.send(IP, PORT, "yes")
                scene.move()
            elif str(message) == "b'turn'":
                self.send(IP, PORT, "yes")
                scene.turn()

