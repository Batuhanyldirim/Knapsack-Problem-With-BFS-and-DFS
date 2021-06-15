"""
This code solves a knapsack problem from given table by using Bredth First Search(BFS) and Depth First Search(DFS) algorithams for given constraints. 
Maximum wight is 420
"""
#BFS Algorithm

max_w = 420 # id, b, w
import copy
import sys
sys.setrecursionlimit(2000)

count = 0

table = {"1":[20,15],
         "2":[40,32],
         "3":[50,60],
         "4":[36,80],
         "5":[26,43],
         "6":[64,120],
         "7":[54,77],
         "8":[18,6],
         "9":[46,93],
         "10":[28,35],
         "11":[25,37]
         }

state = [1,0,0,1,0,0,0,0,0,0,0,0]


queue = []

global best_state

best_state = []
global best_score

best_score = 0


def create_nodes(state):
  num = state[::-1].index(1)
  
  for i in range(num):
    if num !=0:
      nstate = state.copy()
      nstate[12-num+i] = 1
      weight = weight_cal(nstate)
      if weight <= max_w:
        queue.append(nstate.copy())

def weight_cal(state):
  weight = 0
  for i in range(11):
    if state[i+1] == 1:
      weight += table[str(i+1)][1]
  return weight


def score_cal(state):
  sc = 0
  for i in range(11):
    if state[i+1] == 1:
      sc += table[str(i+1)][0]
  return sc


global c
c = 1
def BFS(state):
  global c, best_score
  global best_state
  c +=1
  create_nodes(state)
  
  
  #print("State:",state)
  #print("Queue:",queue)
  #input()
  while queue:
    score = score_cal(state)
    if score > best_score:
      best_state = state.copy()
      best_score = score
    next_state = queue[0].copy()
    queue.pop(0)
    solution = BFS(next_state)
    return solution
    
  return best_state


print(BFS(state)[1:])
print("score:",best_score)
print("Weight:",weight_cal(best_state))

#DFS Algorithm

max_w = 420 # id, b, w
import copy

count = 0

table = {"1":[20,15],
         "2":[40,32],
         "3":[50,60],
         "4":[36,80],
         "5":[26,43],
         "6":[64,120],
         "7":[54,77],
         "8":[18,6],
         "9":[46,93],
         "10":[28,35],
         "11":[25,37]
         }

state = [1,0,0,0,0,0,0,0,0,0,0,0]


global queue
queue = []

best_state = []

global best_score
best_score = 0


def create_nodes(state):
  num = state[::-1].index(1)
  
  for i in range(num):
    if num !=0:
      nstate = state.copy()
      nstate[12-num+i] = 1
      weight = weight_cal(nstate)
      if weight <= max_w:
        queue.append(nstate.copy())

def weight_cal(state):
  weight = 0
  for i in range(11):
    if state[i+1] == 1:
      weight += table[str(i+1)][1]
  return weight


def score_cal(state):
  sc = 0
  for i in range(11):
    if state[i+1] == 1:
      sc += table[str(i+1)][0]
  return sc


global c
c = 1
def BFS(state):
  global c
  global queue
  global best_score
  #print(c)
  c +=1
  queue = []
  create_nodes(state)
  #print("Best score:",best_score)
  
  #print("State:",state)
  #print("Queue:",queue)
  #input()
  if queue:
    score = score_cal(state)
    if score > best_score:
      best_state = state.copy()
      best_score = score
    next_state = queue[0].copy()
    queue.pop()
    solution = BFS(next_state)
    return solution
  else:
    score = score_cal(state)
    if score > best_score:
      best_state = state.copy()
      best_score = score
  
  if score > best_score:
      best_state = state.copy()
      best_score = score
    
  return state


final = BFS(state)
print(final)
print("Best score:",best_score)
print("Weight:",weight_cal(final))





