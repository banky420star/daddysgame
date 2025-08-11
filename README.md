# Car Racing Game

A fun and exciting car racing game built with Python and Pygame! Control your blue car and avoid the red obstacle cars while scoring points.

## Features

- **Smooth Controls**: Use arrow keys to move your car in all directions
- **Dynamic Obstacles**: Red cars spawn randomly and move down the screen
- **Scoring System**: Earn points by avoiding obstacles
- **Pause Functionality**: Press P to pause/resume the game
- **Game Over Screen**: See your final score and restart options
- **Animated Road**: Moving lane markings for a realistic driving experience

## Installation

1. Make sure you have Python 3.6+ installed on your system
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```bash
   python car_racing_game.py
   ```

2. **Controls**:
   - **Arrow Keys**: Move your car (up, down, left, right)
   - **P**: Pause/Resume the game
   - **R**: Restart the game (when game over or anytime)
   - **Q**: Quit the game (when game over)

3. **Objective**:
   - Control the blue car and avoid hitting the red obstacle cars
   - Score points by surviving longer
   - Try to achieve the highest score possible!

## Game Mechanics

- **Player Car**: Blue car that you control
- **Obstacle Cars**: Red cars that spawn randomly in three lanes
- **Road**: Gray road with yellow lane markings that move to create motion
- **Scoring**: +10 points for each obstacle car you successfully avoid
- **Collision Detection**: Game ends when your car hits an obstacle

## System Requirements

- Python 3.6 or higher
- Pygame 2.5.2
- Any modern operating system (Windows, macOS, Linux)

## Troubleshooting

If you encounter any issues:

1. Make sure Python is installed and in your PATH
2. Verify that Pygame is installed correctly: `pip show pygame`
3. Try running with Python 3 explicitly: `python3 car_racing_game.py`

## Development

The game is built with a modular structure:
- `PlayerCar`: Handles player car movement and rendering
- `Obstacle`: Manages obstacle cars
- `Road`: Handles road animation and rendering
- `Game`: Main game loop and state management

Feel free to modify the game constants (speeds, colors, screen size) to customize your experience!

## License

This project is open source and available under the MIT License. 