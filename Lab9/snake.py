import pygame
import random

# Initialize pygame
pygame.init()

# Load background and food images
bg = pygame.image.load('Lab9/image/snakebg.png')
apple = pygame.image.load('Lab9/image/apple.png')

# Set up screen dimensions and cell size
WIDTH, HEIGHT = 548, 483
CELL_SIZE = 20
gridw = WIDTH // CELL_SIZE
gridh = HEIGHT // CELL_SIZE
FPS = 10

# Set up font and create the screen
font = pygame.font.SysFont(None, 25)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
score = 0
level = 1

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define movement directions
RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(gridw // 2, gridh // 2)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        new_tail = (tail[0] - self.direction[0], tail[1] - self.direction[1])
        self.body.append(new_tail)

    def change_direction(self, direction):
        if direction[0] != -self.direction[0] or direction[1] != -self.direction[1]:
            self.direction = direction

    def check_collision(self):
        head = self.body[0]
        if (
            head[0] < 3.5 or head[0] >= gridw - 3.5
            or head[1] < 3.5 or head[1] >= gridh - 3.5
        ):
            return True
        if head in self.body[1:]:
            return True
        return False

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN,(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            

# Food class
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    # Generate random position for food
    def randomize_position(self):
        position = (
            random.randint(4, gridw - 4),
            random.randint(4, gridh - 4)
        )
        while position in snake.body:
            position = (
                random.randint(4, gridw - 4),
                random.randint(4, gridh - 4)
            )
        return position

    # Draw food on the screen
    def draw(self, surface):
        pygame.draw.rect(surface, RED,(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Initialize snake and food
snake = Snake()
food = Food()
running = True

food_timer = 0 # New timer for food disappearing after a certain time

# Main game loop
while running:
    # Draw background
    screen.blit(bg, (0,0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    # Move snake
    snake.move()

    # Check collision with walls or itself
    if snake.check_collision():
        running = False

    # Check if snake eats food
    if snake.body[0] == food.position:
        snake.grow()
        food.position = food.randomize_position()
        food_weight = random.randint(1, 5)  # Random weight for the food
        score += food_weight
        # Check for level up
        if score > 10:
            level += 1
            FPS += 2
        food_timer = 0

    # Food disappearing after a certain time
    food_timer += 1
    if food_timer >= 70:  # 7 seconds
        food.position = food.randomize_position()
        food_timer = 0
        
    # Draw snake and food on screen
    snake.draw(screen)
    food.draw(screen)

    # Display score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 100, 10))

    # Update display and control frame rate
    pygame.display.flip()
    clock.tick(FPS)

# Quit game
pygame.quit()
quit()
