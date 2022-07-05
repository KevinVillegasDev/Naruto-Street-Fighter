import pygame
from fighter import Fighter
pygame.font.init()

pygame.init()

font = pygame.font.SysFont("comicsans", 40)


def renderTextCenteredAt(text, font, color, x, y, screen, allowed_width):
    """Renders text wrapping at a specified width, and centered"""
    words = text.split()
    lines = []
    while len(words) > 0:
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break
        line = ' '.join(line_words)
        lines.append(line)

    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, color)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh


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
naruto_offset_position = [-5, -5]
naruto_data = [naruto_size, naruto_scale, naruto_offset_position]


background_img = pygame.image.load(
    "assets/images/finalvalley-1.png").convert_alpha()

mainmenu_img = pygame.transform.scale(pygame.image.load(
    "assets/images/mainmenu.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

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

# run game function


def run_game():
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


def main_menu():
    screen.blit(mainmenu_img, (0, 0))
    # controls = font.render(
    #     "Game controls are WASD for movement, and abilities are R and T", 1, (0, 0, 0))
    # screen.blit(controls, (200, 200))
    renderTextCenteredAt("Welcome to Naruto Street Fighter!",
                         font, (255, 255, 255), SCREEN_WIDTH / 2, 50, screen, 800)
    renderTextCenteredAt("Game controls are WASD for movement, and abilities are R and T",
                         font, (255, 255, 255), SCREEN_WIDTH / 2, 200, screen, 800)


# game loop to continuously run game and allow characters to be drawn


def main():
    run = True
    main_menu()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_p]:
                run_game()
        pygame.display.update()


if __name__ == "__main__":
    main()
