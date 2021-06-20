import os
import pygame.image
from Game1 import CELL_WIDTH, CELL_HEIGHT


Working_directory = os.path.dirname(__file__)
Assets = os.path.join(Working_directory, 'assets')
ball = pygame.image.load(os.path.join(Assets, 'ball.png'))
ball = pygame.transform.scale(ball, (CELL_WIDTH, CELL_HEIGHT))
