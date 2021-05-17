# -*- coding: utf-8 -*-
"""
Created on Mon May 17 01:30:27 2021

@author: ashwinrathore@ku.edu
"""
#importing the libraries
import pandas as pd
import numpy as np
import random
learning_rate = 0.5

# rewards related to the cell in the map
# empty=1
# jungle=-4
# lion=-10
# treasure = 30

# Initial map of 5*5 : D = Start cell(Dora), E= Empty cell, J = jungle, L = Lion, T - treasure
initial = [['D', 'E', 'L', 'E', 'L'], ['E', 'J', 'E', 'E', 'E'], ['E', 'E', 'E', 'J', 'E'], ['J', 'E', 'E', 'E', 'E'], ['E', 'E', 'L', 'E', 'T'], ]


rewards=[]
learning=[]
transitions=[]
actions=[]

state_transition = np.zeros((25,5))


#Reward matrix is updated for rewards that Dora will get while going 1 state to another
# Rewards if next step is : 0 for invalid move, 1 for empty cell, -4 for jungle, -10 for Lion , 30 fro Treasure
# It is in the form of Up, down, left, right, curr cell for the curr cell. Each array in the list represent on of the cell calculated each column in each row.
rewards= np.array([[ 0, 1, 0, 1, 1 ], 
                  [ 0, -4, 0, -10, 1 ], 
                  [ 0, 1, 1, 1, 1, -10], 
                  [ 0, 1, -10, -10, 1], 
                  [ 0, 1, 1, 0, -10], 
                  [ 0, 1, 0, -4, 1 ], 
                  [ 1, 1, 1, 1, -4], 
                  [ -10, 1, -4, 1, 1 ], 
                  [ 1, -4,1 ,1 ,1 ], 
                  [ -10, 1, 1, 0, 1 ], 
                  [ 1, -4, 0, 1, 1 ], 
                  [ -4, 1, 1, 1, 1 ], 
                  [ 1, 1, 1, -4, 1], 
                  [ 1, 1,1 ,1 ,-4 ], 
                  [ 1, 1, -4, 0, 1], 
                  [ 1, 1, 0, 1, -4], 
                  [ 1, 1, -4, 1, 1], 
                  [ 1, -10, 1, 1, 1], 
                  [ -4, 1, 1, 1, 1  ], 
                  [ 1, 30, 1, 0, 1 ], 
                  [ -4, 0, 0, 1, 1 ], 
                  [ 1, 0, 1, -10, 1 ], 
                  [ 1,0, 1, 1 ,-10 ], 
                  [ 1, 0, -10, 30 ,1 ], 
                  [ 1, 0, 1, 0 ,30 ]])
            


# This matrix has all the possible transitions i.e. next state that can be taken from curr state. It will give the trace of the path.
transitions= np.array([[-1, 5, -1, 1, 0],
                       [-1, 6, 0, 2, 1],
                       [-1, 7, 1, 3, 2],
                       [-1, 8, 2, 4, 3],
                       [-1, 9, 3, -1, 4],
                       [0, 10, -1, 6, 5],
                       [1, 11, 5, 7, 6],
                       [2, 12, 6, 8, 7],
                       [3, 13, 7, 9, 8],
                       [4, 14, 8, -1, 9],
                       [5, 15, -1, 11, 10],
                       [6, 16, 10, 12, 11],
                       [7, 17, 11, 13, 12],
                       [8, 18, 12, 14, 13],
                       [9, 19, 13, -1, 14],
                       [10, 20, -1, 16, 15],
                       [11, 21, 15, 17, 16],
                       [12, 22, 16, 18, 17],
                       [13, 23, 17, 19, 18],
                       [14, 24, 18, -1, 19],
                       [15, -1, -1, 21, 20],
                       [16, -1, 20, 22, 21],
                       [17, -1, 21, 23, 22],
                       [18, -1, 22, 24, 23],
                       [19, -1, 23, -1, 24]
                        ])

# Actions matrix gives what possible actions are there that Dora can take based on the curr state.
actions= np.array([[1, 3, 4],
                   [1, 2, 3, 4],
                   [1, 2, 3, 4],
                   [1, 2, 3, 4],
                   [1, 2, 4],
                   [0, 1, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 4],
                   [0, 1, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 4],
                   [0, 1, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0, 1, 2, 4],
                   [0, 3, 4],
                   [0, 2, 3, 4],
                   [0, 2, 3, 4],
                   [0, 2, 3, 4],
                   [0, 2, 4]])

# The iterations for training are 300 initially
# The iterations should be run untill all the possible value of state-action pair is fulfilled.
for i in range(300):
    #Starting with first state
    start = 0
    curr = start
    
    #Dora will move forward until the goal state is reached
    while curr != 24:
        #Select one state at random from all state
        action = random.choice(actions[curr])
        
        #Go to the next state as a result of the action taken previously
        next_state = transitions[curr][action]
        future_reward = []
        
        #Add rewards and values for current state
        for action_next in actions[next_state]:
            future_reward.append(state_transition[next_state][action_next])
        
        #Select possible next state with the higheset Q-value
        q_state = rewards[curr][action] + learning_rate*max(future_reward)
        
        #Update the Q matrix with new reward value
        state_transition[curr][action] = q_state
        
        #Set the next state as the current state to move forward
        curr = next_state


print(state_transition)

#Converting state_transitions to pandas.dataframe
df = pd.DataFrame(state_transition)


#Printing the optimal route learned by the algorithm.
route = []
state = 0
while state != 24:
    route.append(state)
    row = df.iloc[state]
    direction = row.idxmax(axis=1)
    state = transitions[state][direction]
route.append(state)

print(route)
