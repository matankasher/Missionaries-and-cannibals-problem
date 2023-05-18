# matan kasher maman 15


START = (3, 3, 1, 0, 0, 0)

import heapq
from collections import deque

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

def is_valid_state(state):
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right, boat_right = state

    if missionaries_left < 0 or cannibals_left < 0 or missionaries_right < 0 or cannibals_right < 0:
        return False

    if (missionaries_left > 0 and cannibals_left > missionaries_left) or \
            (missionaries_right > 0 and cannibals_right > missionaries_right):
        return False

    return True

def is_goal_state(state):
    return state == (0, 0, 0, 3, 3, 1)

def get_valid_moves(state):
    moves = []
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right, boat_right = state
    if boat_left == 1:
        for i in range(3):
            for j in range(3):
                # Move i missionaries and j cannibals from the left to the right
                if 0 < i + j <= 2:
                    new_state = (
                        missionaries_left - i,
                        cannibals_left - j,
                        0,
                        missionaries_right + i,
                        cannibals_right + j,
                        1
                    )
                    moves.append(new_state)
    else:
        for i in range(3):
            for j in range(3):
                # Move i missionaries and j cannibals from the right to the left
                if 0 < i + j <= 2:
                    new_state = (
                        missionaries_left + i,
                        cannibals_left + j,
                        1,
                        missionaries_right - i,
                        cannibals_right - j,
                        0
                    )
                    moves.append(new_state)
    valid_moves = []
    for move in moves:
        if is_valid_state(move):
            valid_moves.append(move)
    return valid_moves


def BFS():
    counter = 0 # counter all developed nodes
    start_state = START
    queue = deque([(start_state, [start_state])])
    visited = set([start_state])
    while queue:
        state, path = queue.popleft()
        if is_goal_state(state):
            return counter, path
        counter += 1 # add to developed counter
        next_moves = get_valid_moves(state)
        for move in next_moves:
            if move not in visited:
                visited.add(move)
                queue.append((move, path  + [move]))

    return None

def IDDFS():
    depth_limit = 1
    counter = 0
    while True:
        result, counter = DFS(START, depth_limit , counter) # call to DFS with depth limit
        if result != None:
            return counter, result
        depth_limit += 1

def DFS(state, depth_limit, counter):
    depth = 0
    nodeQueue = Stack()  # stack for dfs , unlike queue for bfs
    visited = set([state])
    nodeQueue.push((state, [state], 0))
    while not nodeQueue.isEmpty():
        state, path,  depth = nodeQueue.pop()

        if is_goal_state(state):
            return path , counter

        if depth < depth_limit:
            counter = counter + 1
            next_moves = get_valid_moves(state)
            for move in next_moves:
                if move not in visited:
                    visited.add(move)
                    nodeQueue.push((move, path + [move], depth + 1))
    return None, counter


def heuristic(state):
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right, boat_right = state
    # We use a simple heuristic that estimates the remaining number of moves needed to reach the goal state.
    return (missionaries_left + cannibals_left)/2

def Astar():
    counter = 0 # counter all developed nodes
    start_state = START
    nodeQueue = PriorityQueue()
    visited = set([start_state])
    nodeQueue.push((start_state,0,[start_state]),0)
    while not nodeQueue.isEmpty():
        state , depth , path = nodeQueue.pop()
        if is_goal_state(state):
            return counter, path
        counter += 1
        visited.add(state)
        next_moves = get_valid_moves(state)
        for move in next_moves:
            if move not in visited:
                nodeQueue.push((move, depth+1, path +[move]), heuristic(move) +depth +1)
                #using priority according  heurustic and depth
    return None

def GBFS():
    counter = 0 # counter all developed nodes
    start_state = START
    nodeQueue = PriorityQueue()
    visited = set([start_state])
    nodeQueue.push((start_state, [start_state]),0)
    while not nodeQueue.isEmpty():
        state, path = nodeQueue.pop()
        if is_goal_state(state):
            return counter, path
        counter += 1
        visited.add(state)
        next_moves = get_valid_moves(state)
        for move in next_moves:
            if move not in visited:
                nodeQueue.push((move, path + [move]), heuristic(move))
    return None




print("Powered by Matan Kasher")

BFS , BFS_Path = BFS()
A, A_Path = Astar()
GBFS, GBFS_Path = GBFS()
iddfs , iddfs_Path= IDDFS()
print("Number of developed nodes in BFS: ", BFS)
print("the path to solution")
print(*BFS_Path, sep="\n")
print("Number of developed nodes in GBFS:", GBFS)
print("the path to solution")
print(*GBFS_Path, sep="\n")
print("Number of developed nodes in A Star:", A)
print("the path to solution")
print(*A_Path, sep="\n")
print("Number of developed nodes in IDDFS", iddfs)
print("the path to solution")
print(*iddfs_Path, sep="\n")
