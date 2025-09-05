import numpy as np
from collections import deque

def bfs_path(maze: np.ndarray, start: tuple, goal: tuple):
    print("BFS algorithm started")
    start = tuple(map(int, np.ravel(start)))
    goal = tuple(map(int, np.ravel(goal)))

    rows, cols = maze.shape
    visited = np.zeros_like(maze, dtype=bool)
    parent = {}
    
    queue = deque([start])
    visited[start] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c = queue.popleft()
        
        if (r, c) == goal:
            path = []
            curr = goal
            while curr != start:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            path.reverse()
            return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols or 4 <= nr < rows and 4 <= nc < cols:
                if not visited[nr, nc] and (maze[nr, nc] == 0 or (nr, nc) == goal) or not visited[nr, nc] and (maze[nr, nc] == 4 or (nr, nc) == goal):
                    visited[nr, nc] = True
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))
    
    return [] 

