import pygame

class Mario:
    def __init__(self, screen, mario_spr):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load(mario_spr)  # Load the background image
        self.rect = self.image.get_rect()  # Get the rect for the image we loaded in
        self.screen = screen
        self.move_right = False
        self.move_left = False
        self.jump = False
        self.crouch = False

    def walk(self): pass

    def run(self): pass

    def jump(self): pass

    def throw(self): pass

    def get_bigger(self): pass

    def get_smaller(self): pass

    def die(self): pass

    def become_fire_mario(self): pass

