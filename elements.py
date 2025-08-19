import pygame


# Initialize pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rectangle and Text Example")

# Set colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)

# Font for text
font = pygame.font.SysFont(None, 48)   # None = default font, 48 = size

# Text to display
text = font.render("Hello Pygame!", True, BLACK)

# Rectangle (x, y, width, height)
rect = pygame.Rect(200, 150, 200, 100)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rect)

    # Draw text
    screen.blit(text, (180, 50))

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
