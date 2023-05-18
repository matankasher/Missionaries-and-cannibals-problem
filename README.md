# Missionaries-and-cannibals-problem

### Phython
### The code was written as part of the Introduction to Artificial Intelligence course

### Problem info
[Missionariesandcannibalsproblem](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem).


### Solution algo
- Breadth-first search
- Iterative deepening depth-first search
- Greedy Best-First Search
- A Star


### Description
   all state are type of tuple with six int ( , , , , , , )  
   with this meanning (missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right, boat_right)

   if boat in left side so : boat_left = 1 , boat_right = 0 .
   if boat in right side so : boat_left = 0 , boat_right = 1 .

   start state = (3, 3, 1, 0, 0, 0)  - all missionaries, cannibals and boat  in the  left side 
   goal state  = (0, 0, 0, 3, 3, 1)  - all missionaries, cannibals and boat  in the  right side 

   functions - 

   is_goal_state: return boolean value if the given state is goal state

   get_valid_moves: generator all the states we can get from given state , every state checked by is_valid_state 
                    , if it ture , insert the state to MOVES list ,return moves list

   is_valid_state: return boolean value if the given state is valid state.


    Data Structure:

    i used stack and priorty queue Data Structure from packman (maman 11)

heuristic function:
    num of missionaries and cannibals in left divided by 2.
    



BFS   -  used queue for state , for every path also saving currect path.
         increase counter for every developed node that extracted form queue.

IDDFS -  used DFS function (same as bfs , just use stack instead of queue).
         DFS also use depth limit , save in the node stack also the node depth, for every extracted node checking his depth .
         IDDFS call DFS with depth limit 0 ,  as long as DFS had not found path to goal state, IDDFS increase the depth limit.

Astar  -  using priority queue , the sort by h(x) +f(x).
         h(x) it's the heuristic
         f(x) it's the currect value (depth = num of moves)

GBFS -  using priority queue , the sort by h(x).
         h(x) it's the heuristic


### Screenshots

- out put
<img src="/screenshot/run Screenshot 1.png" alt="main page"/>
<img src="/screenshot/run Screenshot 2.png" alt="main page"/>


