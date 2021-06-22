import pygame.image
from Constants import *


cell_size = get_cell_size().tuple()
ball = pygame.image.load(os.path.join(Assets, 'ball.png'))
horizontal_road = pygame.image.load(os.path.join(Assets, 'horizontal_road.png'))
vertical_road = pygame.image.load(os.path.join(Assets, 'vertical_road.png'))
crossroad = pygame.image.load(os.path.join(Assets, 'crossroad.png'))
start = pygame.image.load(os.path.join(Assets, 'start.png'))
finish = pygame.image.load(os.path.join(Assets, 'finish.png'))
arrow_down = pygame.image.load(os.path.join(Assets, 'arrow_down.png'))
arrow_left = pygame.image.load(os.path.join(Assets, 'arrow_left.png'))
arrow_up = pygame.image.load(os.path.join(Assets, 'arrow_up.png'))
arrow_right = pygame.image.load(os.path.join(Assets, 'arrow_right.png'))
ball = pygame.transform.smoothscale(ball, cell_size)
horizontal_road = pygame.transform.smoothscale(horizontal_road, cell_size)
vertical_road = pygame.transform.smoothscale(vertical_road, cell_size)
crossroad = pygame.transform.smoothscale(crossroad, cell_size)
start = pygame.transform.smoothscale(start, cell_size)
finish = pygame.transform.smoothscale(finish, cell_size)
arrow_down = pygame.transform.smoothscale(arrow_down, cell_size)
arrow_left = pygame.transform.smoothscale(arrow_left, cell_size)
arrow_up = pygame.transform.smoothscale(arrow_up, cell_size)
arrow_right = pygame.transform.smoothscale(arrow_right, cell_size)
#FIXME
horizontal_road = vertical_road = crossroad
