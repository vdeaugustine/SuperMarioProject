import pygame

class Mario:
    def __init__(self, screen, mario_spr, mario_speed):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load(mario_spr)  # Load the background image
        self.rect = self.image.get_rect()  # Get the rect for the image we loaded in
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.mario_speed = mario_speed
        self.move_right = False
        self.move_left = False
        self.jump = False
        self.crouch = False
        self.run = False
        self.walk = False

    def walk(self): pass

    def run(self): pass

    def jump(self): pass

    def throw(self): pass

    def get_bigger(self): pass

    def get_smaller(self): pass

    def die(self): pass

    def become_fire_mario(self): pass

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.mario_speed
        if self.move_left and self.rect.left > 0:
            self.center -= self.mario_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

