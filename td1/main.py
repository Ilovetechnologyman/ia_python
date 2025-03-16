''''exo1'''
import random as rd 
GRID_SIZE = 5
EMPTY = 'E'
OBSTACLE = 'O'
REWARD = 'R'
AGENT = 'A'

def create_grid():
    grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    x,y = rd.randint(0,GRID_SIZE-1), rd.randint(0,GRID_SIZE-1)
    while (x, y) == (0, 0):
        x,y = rd.randint(0,GRID_SIZE-1), rd.randint(0,GRID_SIZE-1)
        
    grid[x][y] = REWARD
    reward_position = (x,y)
    nb_obstacles = rd.randint(1,GRID_SIZE)
    grid[0][0] = AGENT
    for _ in range(nb_obstacles):
        x,y = rd.randint(0,GRID_SIZE-1), rd.randint(0,GRID_SIZE-1)
        if grid[x][y] == EMPTY:
            grid[x][y] = OBSTACLE
        else : 
            continue
    return grid, reward_position

def display_grid(grid):
    for row in grid:
        print(' '.join(row))

''''ajout de cette fonction pour la visualisation ! '''
def update_grid(grid, agent_position, previous_position):
    grid[previous_position[0]][previous_position[1]] = EMPTY
    grid[agent_position[0]][agent_position[1]] = AGENT

''''exo2'''

class ReflexAgent : 
    def __init__(self, start_pos):
        self.position = start_pos

    def get_adjacent_position(self):
        r,c = self.position
        valid_moves = []
        if r -1 >= 0:
            valid_moves.append((r-1,c))
        if r +1 < GRID_SIZE:
            valid_moves.append((r+1,c))
        if c -1 >= 0:     
            valid_moves.append((r,c-1))
        if c +1 < GRID_SIZE:
            valid_moves.append((r,c+1))
        return valid_moves
    

    def perceive(self,grid):
        perceptions = {}
        valid_moves =  self.get_adjacent_position()
        for i,j in valid_moves:
            if grid[i][j] == OBSTACLE:
                perceptions[(i,j)] = OBSTACLE
            elif grid[i][j] == REWARD:
                perceptions[(i,j)] = REWARD
            else:
                perceptions[(i,j)] = EMPTY
        return perceptions
    
    def decide_action(self, perceptions):
        for position, content in perceptions.items():
            if content == REWARD:
                return position
        valid_moves = [pos for pos, content in perceptions.items() if content != OBSTACLE]
        if valid_moves:
            return rd.choice(valid_moves)
        return None
                                             



    def move(self,action):
        if action:
            self.position = action

def main():
    grid, reward_position = create_grid()
    agent = ReflexAgent((0, 0))
    display_grid(grid)
    print("Initial Position:", agent.position)
    print("Reward Position:", reward_position)
    
    while agent.position != reward_position:
        previous_position = agent.position
        perceptions = agent.perceive(grid)
        action = agent.decide_action(perceptions)
        agent.move(action)
        update_grid(grid, agent.position, previous_position)
        display_grid(grid)
        print("Agent Position:", agent.position)
        print("Reward Position:", reward_position)
        print()

if __name__ == "__main__":
    main()