import pygame
import Game1
from Vector2 import Vector2


def transform_coordinates(coordinate, scalar_x, scalar_y):
    return Vector2(coordinate.x * scalar_x, coordinate.y * scalar_y)


class GameObject(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((Game1.CELL_WIDTH, Game1.CELL_HEIGHT))
        self.rect = self.image.get_rect()
        self._position = position

    def get_position(self):
        return self._position

    def update(self):
        self.rect.topleft = self._position.tuple()

    def move(self, direction, velocity, dt):
        self._position += (direction * velocity * dt)

    def draw(self, painter):
        painter.show(self)
