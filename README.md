# Snake Game

This is a simple Snake game implemented using Python and Pygame.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/2001J/Snake-game
    cd Snake-game
    ```

2. Install the required dependencies:
    ```sh
    pip install pygame
    ```

## Configuration

You can configure the game settings in the `config.py` file. Here are the default settings:

```python
SCREEN_SIZE = 400
FPS = 60
GRID_CELL_SIZE = 20
SNAKE_PART_SIZE = 20
SNAKE_MOVE_LENGTH = 20
FOOD_SIZE = 20

DELAY = 100

BG_COLOR = (34, 40, 49)       # Dark background color
GRID_COLOR = (57, 62, 70)     # Slightly lighter grid color
SNAKE_COLOR = (0, 173, 181)   # Bright cyan snake color
FOOD_COLOR = (238, 238, 238)  # Light food color