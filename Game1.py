import pygame
from Vector2 import Vector2
import Game
import GameObject
import Ball

CELL_WIDTH = 60
CELL_HEIGHT = 60


class Game1(Game.Game):

    def __init__(self):
        super().__init__()
        self._o = Ball.Ball(Vector2(0, 1))

    def load(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
        tmp = GameObject.transform_coordinates(self._o.get_logical_position() + self._o.get_direction(), CELL_WIDTH, CELL_HEIGHT)
        if self._o.get_position().y >= tmp.y:
            self._o.move_in_logical_coordinates(self._o.get_direction())
        self._o.move(Vector2(0, 1), 100, self.get_delta_time())

    def draw(self):
        self._o.draw(self)
