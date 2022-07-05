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

# define colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# define fighter variables
naruto_size = 52
naruto_scale = 4
naruto_data = [naruto_size, naruto_scale]


background_img = pygame.image.load(
    "assets/images/finalvalley-1.png").convert_alpha()

naruto_sprites = pygame.image.load(
    "assets/naruto/sprites/naruto sprites.png").convert_alpha()

# find number of steps in each animation
naruto_steps = [13, 13, 12, 10, 6, 11, 8, 9, 6]
naruto2_steps = [13, 13, 12, 10, 6, 11, 8, 9, 6]


def show_bg():
    scaled_bg = pygame.transform.scale(
        background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# function for health bars


def health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


# create fighter instances
fighter_1 = Fighter(200, 310, naruto_data, naruto_sprites, naruto_steps)
fighter_2 = Fighter(700, 310, naruto_data, naruto_sprites, naruto2_steps)


# game loop to continuously run game and allow characters to be drawn
run = True
while run:
    clock.tick(FPS)
    show_bg()
    health_bar(fighter_1.health, 20, 20)
    health_bar(fighter_2.health, 580, 20)
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    # fighter_2.move()
    fighter_1.show(screen)
    fighter_2.show(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
