import copy

# Heuristic function: Manhattan distance
def hn(state, finalstate):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != -1:
                value = state[i][j]
                goal_pos = divmod(value - 1, 3) if value != 0 else (2, 2)
                distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return distance

# Find position of blank tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == -1:
                return (i, j)

# Move actions
def move_left(state, pos):
    i, j = pos
    if j == 0:
        return None
    new_state = copy.deepcopy(state)
    new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
    return new_state

def move_up(state, pos):
    i, j = pos
    if i == 0:
        return None
    new_state = copy.deepcopy(state)
    new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
    return new_state

def move_right(state, pos):
    i, j = pos
    if j == 2:
        return None
    new_state = copy.deepcopy(state)
    new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
    return new_state

def move_down(state, pos):
    i, j = pos
    if i == 2:
        return None
    new_state = copy.deepcopy(state)
    new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
    return new_state

# Print path
def print_path(path):
    for i, state in enumerate(path):
        print(f"Step {i+1}:")
        for row in state:
            print(row)
        print()

def a_star(initial_state, final_state):
    explored = []
    open_list = [(initial_state, 0)]
    
    while open_list:
        state, gn_val = open_list.pop(0)
        explored.append(state)
        if state == final_state:
            return explored

        pos = find_blank(state)
        actions = [move_left, move_up, move_right, move_down]
        for action in actions:
            new_state = action(state, pos)
            if new_state and new_state not in explored:
                hn_val = hn(new_state, final_state)
                fn_val = gn_val + 1 + hn_val  # g(n) + h(n)
                open_list.append((new_state, gn_val + 1))
                open_list.sort(key=lambda x: x[1] + hn(x[0], final_state))

# Precomputed initial and final states
initial_state = [[1, 2, 3], [-1, 4, 6], [7, 5, 8]]
final_state = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]

# Solve the 8-puzzle problem
path = a_star(initial_state, final_state)
if path:
    print_path(path)
else:
    print("No solution found.")