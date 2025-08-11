# Daddy's Game Collection

A collection of fun games including a car racing game and a couples card game!

## 🚗 Car Racing Game

A fun and exciting car racing game built with Python and Pygame! Control your blue car and avoid the red obstacle cars while scoring points.

### Features

- **Smooth Controls**: Use arrow keys to move your car in all directions
- **Dynamic Obstacles**: Red cars spawn randomly and move down the screen
- **Scoring System**: Earn points by avoiding obstacles
- **Pause Functionality**: Press P to pause/resume the game
- **Game Over Screen**: See your final score and restart options
- **Animated Road**: Moving lane markings for a realistic driving experience

### Installation

1. Make sure you have Python 3.6+ installed on your system
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### How to Play

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

## 💕 Couples Card Game

A turn-based card game designed for couples to strengthen their relationship through questions and challenges rated in different tiers.

### Features

- **Three Tiers**: Beginner, Intermediate, and Advanced levels
- **Two Game Modes**: Questions about each other and relationship challenges
- **Scoring System**: Rate answers and challenges to earn points
- **Turn-based Gameplay**: Players take turns answering questions or completing challenges
- **Multiple Formats**: Available as both Python console game and web browser game

### Game Modes

1. **Questions Mode**: Answer questions about your partner
2. **Challenges Mode**: Complete relationship-building activities together
3. **Mixed Mode**: Combination of both questions and challenges

### Tiers

- **Beginner**: Easy questions about preferences and fun challenges
- **Intermediate**: Deeper questions about fears, dreams, and meaningful challenges
- **Advanced**: Intimate questions about relationship dynamics and personal growth

### How to Play

#### Python Version
```bash
python couples_card_game.py
```

#### Web Version
Open `couples_card_game_web.html` in any web browser.

### Gameplay

1. Enter both players' names
2. Choose your tier (Beginner/Intermediate/Advanced)
3. Select game mode (Questions/Challenges/Mixed)
4. Choose number of rounds (1-10)
5. Take turns answering questions or completing challenges
6. Rate each other's answers/experiences (1-5 stars)
7. See final results and winner

## 🎮 Game Files

- `car_racing_game.py` - Main car racing game (requires pygame)
- `simple_car_game.py` - Simple text-based car game (no dependencies)
- `car_game_text.py` - Advanced text-based car game
- `couples_card_game.py` - Python console version of couples game
- `couples_card_game_web.html` - Web browser version of couples game
- `run_game.sh` - Launcher script for car game
- `requirements.txt` - Python dependencies

## System Requirements

- Python 3.6 or higher (for Python games)
- Pygame 2.5.2 (for car racing game)
- Any modern web browser (for web-based couples game)
- Any modern operating system (Windows, macOS, Linux)

## Troubleshooting

If you encounter any issues:

1. Make sure Python is installed and in your PATH
2. Verify that Pygame is installed correctly: `pip show pygame`
3. Try running with Python 3 explicitly: `python3 car_racing_game.py`
4. For web games, simply open the HTML file in any browser

## Development

The games are built with modular structures:
- **Car Game**: PlayerCar, Obstacle, Road, and Game classes
- **Couples Game**: Tier-based question/challenge system with scoring

Feel free to modify the game constants, add new questions/challenges, or customize the experience!

## License

This project is open source and available under the MIT License.

## GitHub Repository

This project is hosted at: [https://github.com/banky420star/daddysgame.git](https://github.com/banky420star/daddysgame.git) 