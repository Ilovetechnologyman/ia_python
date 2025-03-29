import numpy as np
import matplotlib.pyplot as plt
import time
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

def bfs_maze_solver(maze, start, goal):
    """
    Résolution du labyrinthe avec la recherche en largeur (BFS).
    """
    rows, cols = maze.shape
    queue = [start]  # File (FIFO) pour stocker les positions à explorer
    visited = set()  # Ensemble des positions déjà visitées
    parent = {}  # Dictionnaire pour reconstruire le chemin

    visited.add(start)

    while queue:
        current = queue.pop(0)  # Récupérer la position actuelle

        if current == goal:  # Si l'objectif est atteint
            # Reconstruire le chemin à partir du dictionnaire parent
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            return path[::-1]  # Retourner le chemin dans l'ordre correct

        # Obtenir les voisins valides (haut, bas, gauche, droite)
        x, y = current
        neighbors = [
            (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
        ]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))  # Ajouter les voisins valides à la file
                visited.add((nx, ny))  # Marquer comme visité
                parent[(nx, ny)] = current  # Enregistrer le parent pour reconstruire le chemin

    return None  # Aucun chemin trouvé





import time  # Pour mesurer le temps d'exécution

# Main
if __name__ == "__main__":
    maze = generate_maze(10, 10)
    start = (1, 1)
    goal = (6, 4)

    # Résolution avec DFS
    print("Résolution avec DFS :")
    start_time_dfs = time.time()  # Début du chronométrage pour DFS
    path_dfs = dfs_maze_solver(maze, start, goal)
    end_time_dfs = time.time()  # Fin du chronométrage pour DFS

    if path_dfs:
        print("Chemin trouvé avec DFS :", path_dfs)
        print("Longueur du chemin (DFS) :", len(path_dfs))
        print("Temps d'exécution (DFS) :", end_time_dfs - start_time_dfs, "secondes")
        visualize_maze(maze, path_dfs)
    else:
        print("Aucun chemin trouvé avec DFS.")
        visualize_maze(maze)

    # Résolution avec BFS
    print("\nRésolution avec BFS :")
    start_time_bfs = time.time()  # Début du chronométrage pour BFS
    path_bfs = bfs_maze_solver(maze, start, goal)
    end_time_bfs = time.time()  # Fin du chronométrage pour BFS

    if path_bfs:
        print("Chemin trouvé avec BFS :", path_bfs)
        print("Longueur du chemin (BFS) :", len(path_bfs))
        print("Temps d'exécution (BFS) :", end_time_bfs - start_time_bfs, "secondes")
        visualize_maze(maze, path_bfs)
    else:
        print("Aucun chemin trouvé avec BFS.")
        visualize_maze(maze)

    # Comparaison des performances
    print("\nComparaison des performances :")
    if path_dfs and path_bfs:
        print(f"Longueur du chemin DFS : {len(path_dfs)}")
        print(f"Longueur du chemin BFS : {len(path_bfs)}")
        print(f"Temps d'exécution DFS : {end_time_dfs - start_time_dfs:.6f} secondes")
        print(f"Temps d'exécution BFS : {end_time_bfs - start_time_bfs:.6f} secondes")
    else:
        print("Impossible de comparer les performances, un chemin est manquant.")