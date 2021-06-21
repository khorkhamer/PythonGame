import GameObject
import Resource
from Constants import *


class Arrow(GameObject.GameObject):
    def __init__(self, position, direction):
        super().__init__(GameObject.transform_coordinates(position, get_cell_size().x, get_cell_size().y))
        self._logical_position = position
        self.set_direction(direction)

    def get_logical_position(self):
        return self._logical_position

    def set_position(self, position):
        self._position = position

    def set_direction(self, direction):
        self._direction = direction
        if direction == "up":
            self.image = Resource.arrow_up
        elif direction == "right":
            self.image = Resource.arrow_right
        elif direction == "down":
            self.image = Resource.arrow_down
        else:
            self.image = Resource.arrow_left

    def move(self):
        pass
