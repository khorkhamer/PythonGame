import pygame
import time

WIDTH = 660
HEIGHT = 660
WHITE = (255, 255, 255)


class Game:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._clock = pygame.time.Clock()
        self._prev = time.time()
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

    def draw(self):
        pass

    def show(self, game_object):
        self._all_sprites.add(game_object)

    def _draw(self):
        self.draw()
        self._all_sprites.update()
        self._screen.fill(WHITE)
        self._all_sprites.draw(self._screen)
        pygame.display.flip()

    def update(self):
        pass

    def load(self):
        pass

    def run(self):
        self._prev = time.time()
        while self._running:
            now = time.time()
            self._delta_time = now - self._prev
            self._prev = now
            self.update()
            self._draw()
        pygame.quit()

    def stop(self):
        self._running = False
