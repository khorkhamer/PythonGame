from Vector2 import Vector2
import GameObject
import Resource
import Game1


class Ball(GameObject.GameObject):
    def __init__(self, position):
        super().__init__(GameObject.transform_coordinates(position, Game1.CELL_WIDTH, Game1.CELL_HEIGHT))
        self.image = Resource.ball
        self._logical_position = position
        self._direction = Vector2(0, 1)
        self._velocity = 90

    def get_logical_position(self):
        return self._logical_position

    def get_velocity(self):
        return self._velocity

    def get_direction(self):
        return self._direction

    def set_direction(self, new_direction):
        self._direction = new_direction

    def move_in_logical_coordinates(self, direction):
        self._logical_position += direction
