import pygame
from Constants import *
import Arrow
from Vector2 import Vector2
import json
import Road
import Ball
import GameObject

STATE = {
    "Idle": "Idle",
    "Animating": "Animating",
    "Arrow": "Arrow"
}


class Scene(GameObject.GameObject):
    def __init__(self, uri):
        self._objects = []
        self._ball = None
        self._arrow = None
        self._roads = pygame.sprite.Group()
        self._ball_group = pygame.sprite.Group()
        self._arrow_group = pygame.sprite.Group()
        self._state = STATE["Idle"]
        self._need_draw = True
        self._current_dir = "up"
        self._initialize(uri)

    def get_state(self):
        return self._state

    def _initialize(self, uri):
        with open(uri, "r") as file:
            data = json.load(file)

        def unpack(d, o):
            x = d[o]["position"]["x"]
            y = d[o]["position"]["y"]
            return Vector2(x, y)

        for obj in data:
            tmp = obj[:-1]
            if tmp == "Start":
                pos = unpack(data, obj)
                ball = Ball.Ball(pos)
                ball.set_direction("right")
                arrow = Arrow.Arrow(pos, "right")
                self._arrow_group.add(arrow)
                self._ball_group.add(ball)
                self._ball = ball
                self._arrow = arrow
                road = Road.StartRoad(pos)
                self._roads.add(road)
                self._objects.append(road)
            elif tmp == "Finish":
                road = Road.FinishRoad(unpack(data, obj))
                self._roads.add(road)
                self._objects.append(road)
            elif tmp == "Horizontal":
                road = Road.HorizontalRoad(unpack(data, obj))
                self._roads.add(road)
                self._objects.append(road)
            elif tmp == "Vertical":
                road = Road.VerticalRoad(unpack(data, obj))
                self._roads.add(road)
                self._objects.append(road)
            elif tmp == "Crossroad":
                road = Road.Crossroad(unpack(data, obj))
                self._roads.add(road)
                self._objects.append(road)

    def draw(self, painter):
        self._roads.draw(painter)
        self._ball_group.draw(painter)
        self._arrow_group.draw(painter)
        """
        if self._need_draw:
            for obj in self._objects:
                obj.draw(painter)
            self._need_draw = False
            """

    def update(self):
        pass

    def update(self, dt):
        self._turn_arrow()
        self._move_ball(dt)
        self._roads.update()
        self._ball_group.update()
        self._arrow.set_position(self._ball.get_position())
        self._ball.get_direction()
        self._arrow.set_direction(self._ball.get_direction())
        self._arrow_group.update()

    def _move_ball(self, dt):
        if self._state == STATE["Animating"]:
            dir = self._ball.get_vector_direction()
            tmp = self._ball.get_logical_position() + dir
            tmp = GameObject.transform_coordinates(tmp, get_cell_size().x, get_cell_size().y)
            pos = self._ball.get_position()
            d = self._ball.get_direction()
            if d == "up" and pos.y <= tmp.y:
                self._ball.move_in_logical_coordinates(dir)
                self._state = STATE["Idle"]
            elif d == "right" and pos.x >= tmp.x:
                self._ball.move_in_logical_coordinates(dir)
                self._state = STATE["Idle"]
            elif d == "down" and pos.y >= tmp.y:
                self._ball.move_in_logical_coordinates(dir)
                self._state = STATE["Idle"]
            elif d == "left" and pos.x <= tmp.x:
                self._ball.move_in_logical_coordinates(dir)
                self._state = STATE["Idle"]
            else:
                self._ball.move(dir, self._ball.get_velocity(), dt)

    def _next_dir(self):
        if self._current_dir == "up":
            self._current_dir = "left"
        elif self._current_dir == "left":
            self._current_dir = "down"
        elif self._current_dir == "down":
            self._current_dir = "right"
        elif self._current_dir == "right":
            self._current_dir = "up"

    def _turn_arrow(self):
        if self._state == STATE["Arrow"]:
            pygame.time.wait(500)
            self._state = STATE["Idle"]

    def move(self):
        self._state = STATE["Animating"]

    def turn(self):
        self._ball.set_direction(self._current_dir)
        self._next_dir()
        self._state = STATE["Arrow"]
