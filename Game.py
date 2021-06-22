import pygame
import time
import Controller
from Constants import *


class Game:
    def __init__(self, scene):
        pygame.init()
        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._clock = pygame.time.Clock()
        self._controller = Controller.Controller(MIP, MPORT)
        self._scene = scene
        self._prev_time = time.time()
        self._all_sprites = pygame.sprite.Group()
        self._delta_time = 0
        self._running = True
        pygame.display.set_caption("Python Game")

    def get_screen(self):
        return self._screen

    def get_clock(self):
        return self._clock

    def get_delta_time(self):
        return self._delta_time

    def draw(self, painter):
        pass

    def show(self, game_object):
        self._all_sprites.add(game_object)

    def _draw(self):
        #        self.draw()
        #        self._all_sprites.update()
        self._screen.fill(WHITE)
        #        self._all_sprites.draw(self._screen)
        self.draw(self._screen)
        pygame.display.flip()

    def update(self):
        pass

    def load(self):
        pass

    def run(self):
        self._prev_time = time.time()
        self._controller.start_server()
        while self._running:
            now = time.time()
            self._delta_time = now - self._prev_time
            self._prev_time = now
            self.update()
            self._draw()
#            time.sleep(1)
            if self._controller.queue.exists():
                self._controller.handle(self._controller.queue.get(), self._scene)
        self._controller.stop_server()
        pygame.quit()

    def stop(self):
        self._running = False
