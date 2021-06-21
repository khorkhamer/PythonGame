import pygame
from Vector2 import Vector2
from Constants import *
import Game
import Scene


class Game1(Game.Game):

    def __init__(self):
        super().__init__(Scene.Scene(os.path.join(Working_directory, "scene.json")))
#        self._scene = Scene.Scene(os.path.join(Working_directory, "scene.json"))

    def load(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
        self._scene.update(self.get_delta_time())

    def draw(self, painter):
        self._scene.draw(painter)
