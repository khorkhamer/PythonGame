import os
from Vector2 import Vector2

WIDTH = 660
HEIGHT = 660
WHITE = (255, 255, 255)
Working_directory = os.path.dirname(__file__)
Assets = os.path.join(Working_directory, 'assets')
SCENE = "scenes/scene1.json"
#IP = "192.168.3.16"
IP = "localhost"
PORT = 8887
#MIP = "192.168.3.131"
MIP = IP
MPORT = 8889


def get_cell_size():
    return Vector2(60, 60)
