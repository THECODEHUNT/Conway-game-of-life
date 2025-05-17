# 🧬 Conway's Game of Life – Python + Pygame

This is a visual interactive simulation of Conway’s Game of Life built with **Python** and **Pygame**. It allows you to play, pause, step through generations, and save/load patterns.

## 🚀 How to Run

```bash
pip install pygame
python life.py --width 40 --height 20 --fps 6
```

## 🎮 Controls

| Key     | Action           |
|---------|------------------|
| SPACE   | Play/Pause       |
| N       | Step one frame   |
| C       | Clear grid       |
| R       | Random fill      |
| S       | Save pattern     |
| L       | Load pattern     |

## 📂 File Format – `patterns.txt`

```
# Pattern: Glider
1,0
2,1
0,2
1,2
2,2
```

## 🧪 Testing

Run unit tests:
```bash
pytest tests/test_blinker.py
```

## 🧠 Learning Highlights

- 2D grid simulation with `set[(x, y)]` for state
- Game rules implemented as `next_gen()` function
- Graphical visualisation using `pygame`
- File I/O with save/load
- Unit testing with `pytest`

---
Enjoy the simulation! 🎉
