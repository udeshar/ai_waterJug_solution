from queue import Queue, LifoQueue, PriorityQueue

def get_successors(state, capacities):
    successors = []

    # Filling jug 0
    if(capacities[0] != state[0]):
      successors.append([capacities[0], state[1]])

    # Filling jug 1
    if(capacities[1] != state[1]):
      successors.append([state[0], capacities[1]])

    # Emptying jug 0
    if(state[0] != 0):
      successors.append([0, state[1]])

    # Emptying jug 1
    if(state[1] != 0):
      successors.append([state[0], 0])

    # Pouring water from jug 0 to jug 1
    pour_amount = min(state[0], capacities[1] - state[1])
    successors.append([state[0] - pour_amount, state[1] + pour_amount])

    # Pouring water from jug 1 to jug 0
    pour_amount = min(state[1], capacities[0] - state[0])
    successors.append([state[0] + pour_amount, state[1] - pour_amount])

    return successors

# Breadth-First Search (BFS)
def bfs(initial_state, target_state, capacities):
    visited = set()
    queue = Queue()
    queue.put((initial_state, [initial_state]))  # Storing path as a list

    while not queue.empty():
        current_state, path = queue.get()
        
        if current_state == target_state:
            return path
        
        visited.add(tuple(current_state))
        
        successors = get_successors(current_state, capacities)
        for successor in successors:
            if tuple(successor) not in visited:
                new_path = path + [successor]  # Add the new state to the path
                queue.put((successor, new_path))

    return None

# Depth-First Search (DFS)
def dfs(initial_state, target_state, capacities):
    visited = set()
    stack = LifoQueue()
    stack.put((initial_state, [initial_state]))  # Storing path as a list
    
    while not stack.empty():
        current_state, path = stack.get()
        
        if current_state == target_state:
            return path
        
        visited.add(tuple(current_state))
        
        successors = get_successors(current_state, capacities)
        for successor in successors:
            if tuple(successor) not in visited:
                new_path = path + [successor]  # Add the new state to the path
                stack.put((successor, new_path))
    
    return None

# Hill Climbing
def hill_climbing(initial_state, target_state, capacities):
    current_state = initial_state
    path = [current_state]
    
    while current_state != target_state:
        successors = get_successors(current_state, capacities)
        best_successor = min(successors, key=lambda state: heuristic(state, target_state))
        
        if heuristic(best_successor, target_state) >= heuristic(current_state, target_state):
            break
        
        current_state = best_successor
        path.append(current_state)
    
    return path

# A* Algorithm
def a_star(initial_state, target_state, capacities):
    queue = PriorityQueue()
    queue.put((0, initial_state, [initial_state]))  # Storing path as a list
    visited = set()
    
    while not queue.empty():
        _, current_state, path = queue.get()
        
        if current_state == target_state:
            return path
        
        visited.add(tuple(current_state))
        
        successors = get_successors(current_state, capacities)
        for successor in successors:
            if tuple(successor) not in visited:
                new_path = path + [successor]  # Add the new state to the path
                queue.put((heuristic(successor, target_state) + heuristic(current_state, target_state), successor, new_path))
    
    return None

# Heuristic function for A*
def heuristic(state, target_state):
    return sum(abs(state[i] - target_state[i]) for i in range(len(state)))

# Main code
if __name__ == "__main__":
    capacities = [7, 4]  # Example: Two jugs with capacities 7 and 4
    initial_state = [1, 0]
    target_state = [4, 0]  # Example: Target state
    
    bfs_result = bfs(initial_state, target_state, capacities)
    dfs_result = dfs(initial_state, target_state, capacities)
    hill_climbing_result = hill_climbing(initial_state, target_state, capacities)
    a_star_result = a_star(initial_state, target_state, capacities)
    
    print("BFS:", bfs_result)
    print("DFS:", dfs_result)
    print("Hill Climbing:", hill_climbing_result)
    print("A*:", a_star_result)
