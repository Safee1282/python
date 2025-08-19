import pygame


# Initialize pygame
pygame.init()

# Screen settings
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Two Rectangles Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Sprite positions and sizes
player = pygame.Rect(100, 100, 50, 50)   # Controlled rectangle
enemy = pygame.Rect(300, 200, 50, 50)    # Static rectangle

# Speed of movement
speed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    # Draw rectangles
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLUE, enemy)

    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
