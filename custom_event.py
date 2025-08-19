import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Event")

# Colors
WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        self.image.fill(random.choice(colors))

# Create two sprites
sprite1 = Player((255, 0, 0), 200, 200)
sprite2 = Player((0, 0, 255), 400, 200)

# Sprite group
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Custom event (every 2000ms = 2 seconds)
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event triggered
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Update display
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
