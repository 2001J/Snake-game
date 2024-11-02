import pygame
from pygame import Vector2
from random import randrange
import config

def init_game():
    # Initialize the game and create the screen and clock objects
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
    clock = pygame.time.Clock()
    return screen, clock

def draw_grid(screen):
    # Draw the grid on the screen
    for i in range(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (i, 0), (i, config.SCREEN_SIZE))
        pygame.draw.line(screen, config.GRID_COLOR, (0, i), (config.SCREEN_SIZE, i))

def draw_snake(screen, snake_parts):
    # Draw the snake on the screen
    for snake_part in snake_parts:
        pygame.draw.rect(screen, config.SNAKE_COLOR, snake_part, 8, 4)

def draw_food(screen, food_rect):
    # Draw the food on the screen
    pygame.draw.rect(screen, config.FOOD_COLOR, food_rect, 0, 10)

def handle_events(snake_direction):
    # Handle user input and update the snake's direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return False, snake_direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_direction[1] > 0:
                snake_direction = Vector2(0, -config.SNAKE_MOVE_LENGTH)
            if event.key == pygame.K_DOWN and not snake_direction[1] < 0:
                snake_direction = Vector2(0, config.SNAKE_MOVE_LENGTH)
            if event.key == pygame.K_LEFT and not snake_direction[0] > 0:
                snake_direction = Vector2(-config.SNAKE_MOVE_LENGTH, 0)
            if event.key == pygame.K_RIGHT and not snake_direction[0] < 0:
                snake_direction = Vector2(config.SNAKE_MOVE_LENGTH, 0)
    return True, snake_direction

def main():
    # Main game loop
    screen, clock = init_game()
    running = True
    begin = True
    bait = True
    time = 0
    snake_rect = None
    snake_length = 1
    snake_parts = []
    snake_direction = Vector2(0, 0)
    food_rect = None

    while running:
        if begin:
            # Initialize the snake and food positions
            begin = False
            time = 0
            snake_rect = pygame.rect.Rect(
                [randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
                 randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
                 config.SNAKE_PART_SIZE,
                 config.SNAKE_PART_SIZE])
            snake_length = 1
            snake_parts = []
            snake_direction = Vector2(0, 0)

        if bait:
            # Generate a new food position
            bait = False
            food_rect = pygame.rect.Rect([randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
                                          randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
                                          config.FOOD_SIZE,
                                          config.FOOD_SIZE])

        # Handle events and update the snake's direction
        running, snake_direction = handle_events(snake_direction)

        time_now = pygame.time.get_ticks()

        # Clear the screen and draw the grid
        screen.fill(config.BG_COLOR)
        draw_grid(screen)

        if time_now - time > config.DELAY:
            # Update the snake's position and check for collisions
            time = time_now
            snake_rect.move_ip(snake_direction)
            snake_parts.append(snake_rect.copy())
            snake_parts = snake_parts[-snake_length:]

        # Draw the food and snake
        draw_food(screen, food_rect)
        draw_snake(screen, snake_parts)

        # Check for collisions with the walls or itself
        if (snake_rect.left < 0 or snake_rect.right > config.SCREEN_SIZE or
                snake_rect.top < 0 or snake_rect.bottom > config.SCREEN_SIZE or
                len(snake_parts) != len(set(snake_part.center for snake_part in snake_parts))):
            begin = True

        # Check if the snake has eaten the food
        if snake_rect.center == food_rect.center:
            snake_length += 1
            bait = True

        # Update the display and control the frame rate
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()