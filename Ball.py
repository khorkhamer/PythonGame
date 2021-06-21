from Constants import *
import GameObject
import Resource


class Ball(GameObject.GameObject):
    def __init__(self, position):
        super().__init__(GameObject.transform_coordinates(position, get_cell_size().x, get_cell_size().y))
        self.image = Resource.ball
        self._logical_position = position
        self._direction = Vector2(1, 0)
        self._velocity = 90

    def set_direction(self, d):
        if d == "up":
            self._direction = Vector2(0, -1)
        elif d == "right":
            self._direction = Vector2(1, 0)
        elif d == "down":
            self._direction = Vector2(0, 1)
        else:
            self._direction = Vector2(-1, 0)
        print(self._direction)

    def get_logical_position(self):
        return self._logical_position

    def get_velocity(self):
        return self._velocity

    def get_direction(self):
        dir = self._direction
        if dir.x == 0 and dir.y == -1:
            return "up"
        elif dir.x == 1 and dir.y == 0:
            return "right"
        elif dir.x == 0 and dir.y == 1:
            return "down"
        elif dir.x == -1 and dir.y == 0:
            return "left"

    def get_vector_direction(self):
        return self._direction

    def set_direction(self, new):
        if new == "up":
            self._direction = Vector2(0, -1)
        elif new == "right":
            self._direction = Vector2(1, 0)
        elif new == "down":
            self._direction = Vector2(0, 1)
        else:
            self._direction = Vector2(-1, 0)

    def move_in_logical_coordinates(self, direction):
        self._logical_position += direction
