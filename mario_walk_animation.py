# import pygame
# from pygame.sprite import Sprite
#
# WHITE_COLOR = (255, 255, 255)
#
# pygame.init()
#
# images = list()
# images.append(pygame.image.load('Resources/Sprites/Mario/white-overalls/walk_r_1.png'))
# images.append(pygame.image.load('Resources/Sprites/Mario/white-overalls/walk_r_2.png'))
# images.append(pygame.image.load('Resources/Sprites/Mario/white-overalls/walk_r_3.png'))
# images.append(pygame.image.load('Resources/Sprites/Mario/white-overalls/walk_r_4.png'))
#
# index = 0
#
# screen = pygame.display.set_mode((600, 600))
# clock = pygame.time.Clock()
#
# while True:
#     event = pygame.event.get()
#
#     if event.type == pygame.QUIT:
#         pygame.quit()
#         quit()
#

import pygame

SIZE = WIDTH, HEIGHT = 600, 400  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white')  # The background colod of our window
FPS = 20  # Frames per second


class WalkingMario(pygame.sprite.Sprite):
    def __init__(self):
        super(WalkingMario, self).__init__()

        self.walk_images = list()

        image = ()
        self.walk_images.append(pygame.image.load('Resources/Sprites/Mario/white-overalls/walk_r_1.png'))
        self.walk_images.append(pygame.image.load('Resources/Sprites/Mario/white-overalls/walk_r_2.png'))
        self.walk_images.append(pygame.image.load('Resources/Sprites/Mario/white-overalls/walk_r_3.png'))
        self.walk_images.append(pygame.image.load('Resources/Sprites/Mario/white-overalls/walk_r_4.png'))


        self.index = 0

        self.image = self.walk_images[self.index]

        # self.rect_numbers

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.walk_images):
            self.index = 0

        self.image = self.walk_images[self.index]


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = WalkingMario()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(5) # The higher the number, the faster he walks


if __name__ == '__main__':
    main()