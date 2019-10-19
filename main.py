import pygame
from pygame.sprite import Group
from level import Level

# 1580x460 is roughly the size of the aspect ratio of the demo game we were given
screen_width = 1580
screen_height = 460


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
    BACKGROUND_COLOR = pygame.Color('white')



    # Initialize the level we are on
    # level = Level(level_dict[level_counter])
    while True:
        pass


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Super Mario')
BACKGROUND_COLOR = pygame.Color('white')


def mario_walk(direction, passed_screen, bgc):
    images = []
    if direction == 'left':
        pass
    if direction == 'right':
        images.append(pygame.image.load('Resources/Sprites/Mario/walk_r_1.png'))
        images.append(pygame.image.load('Resources/Sprites/Mario/walk_r_2.png'))
        images.append(pygame.image.load('Resources/Sprites/Mario/walk_r_3.png'))
        images.append(pygame.image.load('Resources/Sprites/Mario/walk_r_4.png'))

    index = 0
    image = images[index]
    rect = image.get_rect()

    def update(passed_index, passed_images):
        passed_index += 1
        if passed_index >= len(images):
            passed_index = 0
        new_image = passed_images[passed_index]
        return passed_index, new_image

    mario_sprite = pygame.sprite.Sprite()
    m_group = pygame.sprite.Group(mario_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        m_group.update()
        passed_screen.fill(bgc)
        m_group.draw(passed_screen)
        pygame.display.update()
        clock.tick(10)


# run_game()

mario_walk('right', screen, BACKGROUND_COLOR)