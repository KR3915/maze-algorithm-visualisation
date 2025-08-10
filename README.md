
# Maze Algorithm Visualisation

Visual interactive grid editor and pathfinding visualizer using BFS (Breadth-First Search) algorithm, built with Python and Pygame.

## Features

- Grid editor with customizable cells:
  - White (obstacle)
  - Red (start point)
  - Blue (goal point)
  - Eraser to clear cells
- Toolbar with buttons for selecting tools and clearing the grid
- Real-time BFS pathfinding visualization (green path)
- Clear visualization of grid and path
- Separate info window (`info.py`) (optional)

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/news) library
- NumPy

## Installation

```bash
pip install pygame numpy
```

## Usage

Run the main program:

```bash
python main.py
```

### Controls

- Click toolbar buttons to select tools:
  - White brush (obstacle)
  - Red brush (start)
  - Blue brush (goal)
  - Eraser
  - Clear grid
  - Open info window (`info.py`)
- Click cells in the grid to apply selected tool
- Path between start and goal updates automatically

## How it works

- The grid is a NumPy array where each cell's value represents its type:
  - 0 = empty
  - 1 = obstacle (white)
  - 2 = start (red)
  - 3 = goal (blue)
  - 4 = path (green)
- BFS is used to find the shortest path from start to goal avoiding obstacles.
- Path cells are highlighted in green.

## File Structure

- `main.py` — Main program with GUI and logic
- `info.py` — Optional separate info window (launched from toolbar)

## License

MIT License — free to use and modify
