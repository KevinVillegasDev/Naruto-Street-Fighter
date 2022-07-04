from turtle import screensize
import pygame


class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0

    def move(self, screen_width, screen_height):
        speed = 10
        gravity = 2
        # dx and dy are the change in x and y coordinates
        dx = 0
        dy = 0

        # get keypresses
        key = pygame.key.get_pressed()

        # movement
        if key[pygame.K_a]:
            dx = -speed
        if key[pygame.K_d]:
            dx = speed

        # jump
        if key[pygame.K_w]:
            self.vel_y = -30

        # apply gravity to bring fighter down
        self.vel_y += gravity
        dy += self.vel_y

        # ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left

        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        if self.rect.bottom + dy > screen_height - 59:
            self.vel_y = 0
            dy = screen_height - 59 - self.rect.bottom
        # update player position
        self.rect.x += dx
        self.rect.y += dy

    def show(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
