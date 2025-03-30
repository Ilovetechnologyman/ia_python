import time
import numpy as np
import matplotlib.pyplot as plt
from mazelib import Maze
from mazelib.generate. Prims import Prims
from collections import deque

# Random Maze

m = Maze()
m.generator = Prims (10, 10) #TODO: Adjust size if needed
m.generate()
maze_grid = m.grid

# Print the Maze Grid

for row in maze_grid:
    print(" ".join(str(cell) for cell in row)) #TODO: Format nicely

# Visualize the Maze
def visualize_maze(grid, path_dfs=None, path_bfs=None, start = None, end=None):
    plt.imshow(grid, cmap="binary") # TODO: Try different color maps if needed

    if start:
        plt.plot(start[1], start[0], 'bo')
    # Marquer le point d'arrivée en jaune
    if end:
        plt.plot(end[1], end[0], 'yo')  # 'yo' pour un point jaune


    if path_dfs:
        if path_bfs:
            for step in path_dfs:
                if step != start and step != end and step not in path_bfs:
                    plt.plot(step[1], step[0], 'ro')  # Marquer le chemin en rouge
                if step in path_bfs:
                    plt.plot(step[1], step[0],"o",color='purple')  # Marquer le chemin en violet
        else:
            for step in path_dfs:
                if step != start and step != end and step:
                    plt.plot(step[1], step[0], 'ro')  # Marquer le chemin en rouge
    if path_bfs:
        if path_dfs:
            for step in path_bfs:
                if step != start and step != end and step not in path_dfs:
                    plt.plot(step[1], step[0],"o", color='green')  # Marquer le chemin en rouge
                if step in path_dfs:
                    plt.plot(step[1], step[0], "o",color='purple')  # Marquer le chemin en violet
    
    
    plt.xticks([]) #Hide axis
    plt.yticks([])
    plt.title("Generated Maze")
    plt.show()

# Implémentation de DFS
def dfs(maze, start, end):
    stack = [start]
    visited = set()
    path = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        path.append(current)

        if current == end:
            return path

        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and maze[nx, ny] == 0:
                stack.append((nx, ny))

    return None


def bfs(maze, start, end):
    queue = deque([start])
    visited = set()
    path = []
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        path.append(current)

        if current == end:
            return path
        
        x,y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y +dy
            if (0 <= nx < maze.shape[0] and
                0 <= ny < maze.shape[1] and
                maze[nx, ny] == 0 and
                (nx, ny) not in visited):
                queue.append((nx, ny))
                parent[(nx, ny)] = current  # Garder une trace du parent
    return None

# Définir les points de départ et d'arrivée
start = (1, 1)
end = (19, 19)


start_dfs = time.time()
# Exécuter DFS
path_dfs = dfs(np.array(maze_grid), start, end)
end_dfs = time.time()



start_bfs = time.time()
path_bfs = bfs(np.array(maze_grid), start, end)
end_bfs = time.time()

print("DFS : "+str(end_dfs-start_dfs)+"s")
print("BFS : "+str(end_bfs-start_bfs)+"s")
# Visualiser le labyrinthe avec le chemin
visualize_maze(maze_grid, path_dfs, path_bfs, start, end)
