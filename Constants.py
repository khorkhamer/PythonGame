import os
from Vector2 import Vector2

WIDTH = 660
HEIGHT = 660
WHITE = (255, 255, 255)
Working_directory = os.path.dirname(__file__)
Assets = os.path.join(Working_directory, 'assets')
IP = "localhost"
PORT = 8887
MPORT = 8889


def get_cell_size():
    return Vector2(60, 60)
