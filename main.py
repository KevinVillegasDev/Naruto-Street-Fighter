import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Naruto Street Fighter")

# set framerate
clock = pygame.time.Clock()
FPS = 60

background_img = pygame.image.load(
    "assets/images/finalvalley-1.png").convert_alpha()


def show_bg():
    scaled_bg = pygame.transform.scale(
        background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# create fighter instances
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)


# game loop to continuously run game and allow characters to be drawn
run = True
while run:
    clock.tick(FPS)
    show_bg()
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    # fighter_2.move()
    fighter_1.show(screen)
    fighter_2.show(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
