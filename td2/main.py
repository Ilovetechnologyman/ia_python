import numpy as np
import matplotlib.pyplot as plt
from mazelib import Maze
from mazelib.generate.Prims import Prims

# Générer un labyrinthe aléatoire
def generate_maze(rows, cols):
    m = Maze()
    m.generator = Prims(rows, cols)
    m.generate()
    return np.array(m.grid)

# Visualiser le labyrinthe
def visualize_maze(grid, path=None):
    plt.imshow(grid, cmap="binary")
    plt.xticks([])  
    plt.yticks([])
    plt.title("Generated Maze")
    
   
    if path:
        for (x, y) in path:
            plt.plot(y, x, "ro")  
    plt.show()

# Implémentation de la recherche en profondeur (DFS)
def dfs_maze_solver(maze, start, goal):
    rows, cols = maze.shape
    stack = [start]  
    visited = set()  
    path = []  

    while stack:
        current = stack.pop()  
        path.append(current)

        if current == goal:  
            return path

        visited.add(current)

        # Obtenir les voisins valides (haut, bas, gauche, droite)
        x, y = current
        neighbors = [
            (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
        ]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny)) 

    return None  

# Main
if __name__ == "__main__":
   
    maze = generate_maze(10, 10)
    start = (1, 1) 
    goal = (3, 1) 

    # Résoudre le labyrinthe avec DFS
    path = dfs_maze_solver(maze, start, goal)

    if path:
        print("Chemin trouvé :", path)
        visualize_maze(maze, path)
    else:
        print("Aucun chemin trouvé.")
        visualize_maze(maze)