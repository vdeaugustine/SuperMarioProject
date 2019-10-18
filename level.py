import pygame
from background import Background


class Level:
    def __init__(self, level_name):
        # Attribute level_name is assigned to the value that was passed as argument
        self.level_name = level_name
        # String interpolation to get the path we need to load image
        level_path_string = f'sprite_sheets_super_mario/bg-{self.level_name}.png'
        print(level_path_string)
        # Attribute background is a new Background object
        # We are passing the appropriate image path as an argument so it can build
        #   the correct background
        self.background = Background(level_path_string)
