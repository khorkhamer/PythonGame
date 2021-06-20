import os
import pygame.image


Working_directory = os.path.dirname(__file__)
Assets = os.path.join(Working_directory, 'assets')
ball = pygame.image.load(os.path.join(Assets, 'ball.png'))
ball = pygame.transform.scale(ball, (60, 60))
