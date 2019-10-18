import pygame
from pygame.sprite import Group
from level import Level

screen_height = 400
screen_width = 600

# Level dictionary will be used with level counter to know what level we are on
# and what its name is
level_counter = 1
level_dict = {1: '1-1', 2: '1-2', 3: '1-3', 4: '1-4', 5: '2-1', 6: '2-2', 7: '2-3',
              8: '2-4'}


def run_game():
    # Initialize pygame
    pygame.init()
    # Set up a screen and give it the dimensions we want
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Super Mario')

    # Initialize the level we are on
    level = Level(level_dict[level_counter])
    while True:
        pass
run_game()