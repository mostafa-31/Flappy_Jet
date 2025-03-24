

# Plane Crash - A Flappy Bird Style Game

## Description
**Plane Crash** is an engaging side-scrolling game inspired by Flappy Bird. Players control a small plane (currently represented as a bird) and navigate through obstacles (skyscrapers) by jumping and avoiding crashes. The game features real-time scoring, explosion effects upon collision, and a game-over popup with a high score tracking system.

## Features
- **Simple and Addictive Gameplay**: Press the spacebar to keep the bird/plane flying and avoid crashing.
- **Randomized Obstacles**: Skyscrapers appear at different heights to keep the game challenging.
- **Realistic Gravity and Jump Mechanics**: The plane falls due to gravity and jumps when the spacebar is pressed.
- **Game Over Screen**: Displays the player's score, highest score, and a "Play Again" button.
- **Explosion Effect**: A visual explosion appears at the collision point.
- **Background Music & Sound Effects**: Game over sound plays upon collision.

## Installation and Setup
1. Ensure you have **Python 3** and **Pygame** installed. If not, install Pygame using:
   ```sh
   pip install pygame
   ```
2. Download or clone this repository.
   ```sh
   git clone https://github.com/mostafa-31/Flappy_Jet.git
   cd Flappy_Jet
   ```
3. Place the following assets in the same directory as the script:
   - `bird.png` (image for the player)
   - `skyscraper.png` (image for obstacles)
   - `bg2.jpg` (background image)
   - `ex3.png` (explosion image)
   - `audio2.mp3` (game-over sound effect)
4. Run the game:
   ```sh
   python game.py
   ```

## Controls
- **Spacebar**: Make the plane jump.
- **R Key**: Restart the game after a game over.
- **Mouse Click**: Click the "Play Again" button after a game over to restart.

## Game Logic
1. The plane starts in the middle of the screen.
2. Skyscrapers move from right to left at a fixed speed.
3. Collision detection is based on pixel masks to ensure precise impact checking.
4. If the plane touches a skyscraper or the screen boundaries, an explosion occurs, and the game over screen is displayed.
5. The game-over screen includes the player’s score, highest score, and a "Play Again" button.

## Future Improvements
- Change the bird sprite to an actual **plane** model.
- Add more sound effects and background music.
- Introduce different difficulty levels.
- Implement power-ups and additional obstacles.

## Author
Developed by **S M Utshab**.

Enjoy playing **Plane Crash**! 🚀
