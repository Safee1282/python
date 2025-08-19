import pygame
import random


# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Load background image (replace with your image path)
background = pygame.image.load("bg.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load sound (replace with your sound path)
collision_sound = pygame.mixer.Sound(".mp3")

# Colors
WHITE = (255, 255, 255)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))   # Blue player
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))   # Red enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 40)
        self.rect.y = random.randint(0, HEIGHT - 40)

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Add 7 enemies
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    # Update player
    all_sprites.update()

    # Check collisions
    hits = pygame.sprite.spritecollide(player, enemies, False)
    for hit in hits:
        score += 1
        collision_sound.play()
        # Move enemy to new random position
        hit.rect.x = random.randint(0, WIDTH - 40)
        hit.rect.y = random.randint(0, HEIGHT - 40)

    # Draw everything
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)