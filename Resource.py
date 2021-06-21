import os
import pygame.image
from Game1 import CELL_WIDTH, CELL_HEIGHT


Working_directory = os.path.dirname(__file__)
Assets = os.path.join(Working_directory, 'assets')
ball = pygame.image.load(os.path.join(Assets, 'ball.png')).convert()
horizontal_road = pygame.image.load(os.path.join(Assets, 'horizontal_road.jpg')).convert()
vertical_road = pygame.image.load(os.path.join(Assets, 'vertical_road.jpg')).convert()
crossroad = pygame.image.load(os.path.join(Assets, 'crossroad.png')).convert()
ball = pygame.transform.smoothscale(ball, (CELL_WIDTH, CELL_HEIGHT))
horizontal_road = pygame.transform.smoothscale(horizontal_road, (CELL_WIDTH, CELL_HEIGHT))
vertical_road = pygame.transform.smoothscale(vertical_road, (CELL_WIDTH, CELL_HEIGHT))
crossroad = pygame.transform.smoothscale(crossroad, (CELL_WIDTH, CELL_HEIGHT))
