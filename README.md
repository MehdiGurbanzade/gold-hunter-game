# Gold Hunter Game

Collect 10 gold coins, avoid the monsters and reach the exit door. A small arcade game written in Python with Pygame.

## Highlights

- **Three difficulty levels**: Easy (2 monsters, speed 2), Medium (4 monsters, speed 3), Hard (6 monsters, speed 4)
- **Bouncing monsters** that move diagonally and reflect off the red walls
- **Win condition**: after the 10th coin the coin disappears and a door spawns at a random position. Reach it to win.
- **Lose condition**: touching any monster ends the game
- **End screen** with final score and Restart / Exit buttons

## Controls

| Key / Action | Effect |
|---|---|
| `1`, `2`, `3` | Choose Easy, Medium or Hard on the start screen |
| Arrow keys | Set the robot's direction (it keeps moving until you press another arrow) |
| Mouse click on **Restart** | Start a new game from the menu |
| Mouse click on **Exit** or close the window | Quit |

## Project structure

| File | Description |
|---|---|
| `main.py` | Complete game: menu, game loop, movement, collisions, end screen |
| `robot.png` | Player sprite |
| `coin.png` | Coin sprite |
| `monster.png` | Monster sprite |
| `door.png` | Exit door sprite |
| `requirements.txt` | Python dependencies (pygame-ce) |

## How to run

```bash
cd gold-hunter-game
pip install -r requirements.txt
python main.py
```

Run all commands from inside the project folder: `requirements.txt` is there, and the images are loaded with relative paths.

The requirements use [pygame-ce](https://pyga.me/), the community edition of Pygame. It is a drop-in replacement (the code still uses `import pygame`) and provides builds for current Python versions, including 3.14. Do not install `pygame` and `pygame-ce` in the same environment.

## Limitations and next steps

- The robot keeps moving in its last direction and stops only at a wall, which can make close calls hard to avoid.
- Coins and the door can spawn on top of a monster.
- Restart calls the menu recursively. Very many restarts in one session will eventually hit Python's recursion limit.
- Ideas: sound effects, a high-score file, levels with walls or obstacles, and a timer.

**Author:** Mehdi Gurbanzade · M.Sc. Data Science
