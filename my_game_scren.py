import pygame


# Initialize pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title of the window
pygame.display.set_caption("My First Game Screen")

# Set background color (RGB: red, green, blue)
background_color = (0, 150, 200)  # light blue

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # close button
            running = False

    # Fill the screen with background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
