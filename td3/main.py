from collections import deque

grid = [
    ['s', 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 'G']
]

# Initialiser grid_eval avec des zéros
grid_eval = [[0 for _ in range(5)] for _ in range(5)]

# Coordonnées du point de départ (s) et du but (G)
start = (0, 0)
goal = (4, 4)

def h(x,y, goal):
    return abs(x-goal[0]) + abs(y-goal[1])

def g(start, grid):
    g_values = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    g_values[start[0]][start[1]] = 0
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
                if g_values[nx][ny] == float('inf'):
                    g_values[nx][ny] = g_values[x][y] + 1
                    queue.append((nx, ny))  # Ajouter le voisin à la file d'attente
    return g_values

def a_star(grid, grid_eval, start, goal):
    g_values = g(start, grid)
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y]!=1:
                grid_eval[x][y] = g_values[x][y] + h(x, y, goal)


def print_grid(grid):
    for row in grid:
        print(" ".join(f"{cell:2}" if isinstance(cell, int) else f"{cell:2}" for cell in row))
    print("\n")

a_star(grid, grid_eval, start, goal)
print_grid(grid_eval)
