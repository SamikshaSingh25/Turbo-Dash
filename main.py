import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CAR_WIDTH, CAR_HEIGHT = 60, 100
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
FPS = 60

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race Car Game")
clock = pygame.time.Clock()

# Load images
car_img = pygame.image.load('car.png')
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))

# Game variables
car_x = (WIDTH - CAR_WIDTH) // 2
car_y = HEIGHT - CAR_HEIGHT - 20
car_speed = 5

obstacle_speed = 5
obstacle_gap = 200
obstacle_width = OBSTACLE_WIDTH
obstacle_height = OBSTACLE_HEIGHT
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
score = 0

# Fonts
font = pygame.font.SysFont(None, 40)

# Functions
def draw_car(x, y):
    screen.blit(car_img, (x, y))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def game_over():
    font_game_over = pygame.font.SysFont(None, 80)
    game_over_text = font_game_over.render("Game Over", True, BLACK)
    screen.blit(game_over_text, (WIDTH//2 - 200, HEIGHT//2 - 50))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > car_speed:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH - car_speed:
        car_x += car_speed

    # Draw car
    draw_car(car_x, car_y)

    # Draw obstacles
    draw_obstacle(obstacle_x, obstacle_y)
    obstacle_y += obstacle_speed

    # Score
    draw_score(score)

    # Collision detection
    if car_y < obstacle_y + obstacle_height:
        if car_x > obstacle_x and car_x < obstacle_x + obstacle_width or car_x + CAR_WIDTH > obstacle_x and car_x + CAR_WIDTH < obstacle_x + obstacle_width:
            game_over()
            pygame.display.update()
            pygame.time.delay(2000)  # Delay for 2 seconds
            running = False

    # Spawn new obstacles
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        score += 1

    # Update the display
    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
