import pygame
import GameObject
import Game1


class Road(GameObject.GameObject):
    def __init__(self, position):
        super().__init__(GameObject.transform_coordinates(position, Game1.CELL_WIDTH, Game1.CELL_HEIGHT))
        self._logical_position = position

    def get_position(self):
        return self._logical_position

    def move(self, direction, velocity, dt):
        pass

    def update(self):
        pass
