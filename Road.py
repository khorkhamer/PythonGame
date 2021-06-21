import pygame
import GameObject
import Resource
from Constants import *


class Road(GameObject.GameObject):
    def __init__(self, position, image):
        super().__init__(GameObject.transform_coordinates(position, get_cell_size().x, get_cell_size().y))
        self.image = image
        self._logical_position = position

    def get_logical_position(self):
        return self._logical_position

    def move(self, direction, velocity, dt):
        pass


class HorizontalRoad(Road):
    def __init__(self, position):
        super().__init__(position, Resource.horizontal_road)


class VerticalRoad(Road):
    def __init__(self, position):
        super().__init__(position, Resource.vertical_road)


class Crossroad(Road):
    def __init__(self, position):
        super().__init__(position, Resource.crossroad)


class StartRoad(Road):
    def __init__(self, position):
        super().__init__(position, Resource.start)


class FinishRoad(Road):
    def __init__(self, position):
        super().__init__(position, Resource.finish)
