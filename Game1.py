import os

import pygame
import json
from Constants import *
import Game
import Scene


class Game1(Game.Game):

    def __init__(self):
        super().__init__(Scene.Scene(os.path.join(Working_directory, SCENE), self.reset))
        self._path = os.path.join(Working_directory, 'config.json')
        with open(self._path, "r") as file:
            self._scenes = json.load(file)
        tmp = []
        for i in self._scenes.values():
            tmp.append(i)
        self._scenes = tmp
        self._scene_idx = 0
        self._scene_path = os.path.join(Working_directory, 'scenes', self._scenes[self._scene_idx])
#        self._scene = Scene.Scene(os.path.join(Working_directory, "scene.json"))

    def reset(self):
        new_scene = self._scene_path
        if os.path.exists(new_scene):
            del self._scene
            self._scene = Scene.Scene(new_scene, self.reset)

    def next_scene(self):
        if self._scene_idx < len(self._scenes) - 1:
            self._scene_idx += 1
        else:
            self._scene_idx = 0
        self._scene_path = os.path.join(Working_directory, 'scenes', self._scenes[self._scene_idx])
        self.reset()

    def load(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset()
                    pygame.time.wait(500)
                elif event.key == pygame.K_e:
                    self.next_scene()
                    pygame.time.wait(500)
#        self._over = self._scene.game_over()
        self._scene.update(self.get_delta_time())

    def draw(self, painter):
        self._scene.draw(painter)
