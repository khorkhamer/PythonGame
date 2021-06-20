import pygame
from Vector2 import Vector2
import GameObject

STATE = {
    "Idle": "Idle",
    "Animating": "Animating"
}


class Scene(GameObject.GameObject):
    def __init__(self):
        self._objects = []
        self._state = STATE["Idle"]

    def draw(self, painter):
        for obj in self._objects:
            obj.draw(painter)

    def update(self):
        pass
