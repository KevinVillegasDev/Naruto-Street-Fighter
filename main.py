from turtle import back
import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Naruto Street Fighter")

background_img = pygame.image.load(
    "assets/images/hiddensandbg.png").convert_alpha()


def show_bg():
    scaled_bg = pygame.transform.scale(
        background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# game loop to continuously run game and allow characters to be drawn
run = True
while run:
    show_bg()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
