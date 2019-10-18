import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, background_image, location=(0, 0)):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load(background_image)  # Load the background image
        self.rect = self.image.get_rect()  # Get the rect for the image we loaded in
        self.rect.left, self.rect.top = location  # Set where the image will be placed
