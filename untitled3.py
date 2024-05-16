# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 22:48:24 2024

@author: roozb
"""

import random
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd

start_time = time.time()
# we set some important costant that will define our network
N=1500   #number hhs
alfa=0.2   # 20% of inhibitors
q=0.02   # probability of connection between two nodes
k=N*q      # with the average connection on each node to the others
time_steps=1000
landa=1
sigma=landa/(k*(1-2*alfa))
seed = 70  # seed random number generators for reproducibility


# neuron_states = np.zeros((N, time_steps)) ####################################################################new


# we decide randomly if the neurons are active(1) or inhibitors(-1)
# memory_cells=int(N*(1-alfa))*[1]+int(N*alfa)*[-1]
# random.shuffle(memory_cells)
# Use seed for reproducibility
random.seed(seed)  # Seed random number generator
G = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        if random.random() < q:
            strength = random.uniform(0, 2 * sigma)
            G[i][j] = strength
# memory_cells=[random.choice(list_cells) for i in range(N)]
inhibitory_nodes = random.sample(range(N), int(alfa * N))
G[:, inhibitory_nodes] *= -1
matrix= G
matrix=np.transpose(matrix)

# Initial states of neurons
initial_states = np.zeros(N)
initial_states[:50]=1  # Set initial states of first 5 neurons to 1
memory_t=initial_states #GitHub add11111111111111111111111111111111111111111111111111111111111111


def multiply (matrix, lis):
  a = np.array(matrix)
  b = np.array(lis)
  s_list = np.dot(b,a) #product vector for matrix and it works properly
  return s_list

order_parameter=[] # total number of neurons activated at each time step (S in the paper)
for j in range(time_steps):
    prob_list=multiply(matrix,memory_t)
    for i in range(N):
        if prob_list[i]>=random.random(): #random number from 0 to 1
            memory_t[i]=1
            # neuron_states[i][j]=1 ####################################################################new
        else:
            memory_t[i]=0
    order_parameter.append(sum(memory_t)) ######################in plot order parameter is something between 0 and 1
    
plt.ylim(0,N)
plt.plot(order_parameter)
plt.xlabel("Time steps", size=12)
plt.ylabel("Order Parameter S", size=12)

plt.title("lambda={} and alpha={}, seed={}, q={}".format(landa,alfa,seed,q))
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))




import statistics as sts

# df=pd.DataFrame(order_parameter)

# df1=pd.DataFrame(neuron_states)

# df.to_csv('OP_subcritical.csv', index=False)

# df1.to_csv('NS_subcritical.csv', index=False)

# order_parameter=pd.read_csv('OrderParameter.csv')
# order_parameter=order_parameter.values.transpose()
# order_parameter=order_parameter[0]


# threshold = sts.mean(order_parameter)
# avalanches = order_parameter > threshold
# avalanche_sizes = []
# current_size = 0
# for activity in avalanches:
#     if activity:
#         current_size += 1
#     elif current_size > 0:
#         avalanche_sizes.append(current_size)
#         current_size = 0
# sizes, counts = np.unique(avalanche_sizes, return_counts=True)
# probabilities = counts / counts.sum()


# plt.loglog(sizes, probabilities, 'o')
# plt.xlabel('Avalanche Duration')
# plt.ylabel('Probability')
# plt.title('Avalanche Size Distribution')
# plt.grid(True, which="both", ls="--")
# plt.legend(['Your Legend'])
# plt.show()
# plt.show()


# #------------------------------------------------------------
# threshold = sts.mean(order_parameter)
# avalanches = order_parameter > threshold
# avalanches_sizes = []
# current_size = 0
# for i in range(len(order_parameter)):
#     if avalanches[i]:
#         current_size += order_parameter[i]
#     elif current_size > 0: 
#         avalanches_sizes.append(current_size-threshold)
#         current_size = 0
# sizes, counts = np.unique(avalanches_sizes, return_counts=True)
# prob_size = counts / counts.sum()
# plt.loglog(sizes, prob_size, 'o')
# # plt.plot(sizes, model_size, color='red', linestyle='--', label='power law')
# plt.xlabel('Avalanche Size')
# plt.ylabel('Probability')
# plt.title('Avalanche Size Distribution')
# plt.grid(True, which="both", ls="--")
# #plt.legend(['Your Legend'])
# plt.show()

# 

# #defining avalanches sizes
# threshold = sts.mean(order_parameter)
# activity = order_parameter > threshold
# avalanches_sizes = []
# current_size = 0
# for i in range(len(activity)):
#     if activity[i]:
#         current_size = current_size + order_parameter[i] - threshold
#     elif current_size > 0: 
#         avalanches_sizes.append(current_size)
#         current_size = 0
# sizes, counts = np.unique(avalanches_sizes, return_counts=True)
# prob_size = counts / counts.sum()



# model_size = sizes**(-3/2)
# plt.loglog(sizes, prob_size, 'o')
# plt.plot(sizes, model_size, color='red', linestyle='--', label='power law')
# plt.xlabel('Avalanche Size')
# plt.ylabel('Probability')
# plt.title('Avalanche Size Distribution')
# plt.grid(True, which="both", ls="--")
# #plt.legend(['Your Legend'])
# plt.show()

#----------------------------------------------------------------




# # Placeholder for your time series data
# data = order_parameter*N  # Replace [...] with your actual data

# # Define the threshold value based on Figure 5
# threshold_value = sts.mean(order_parameter)

# # Identify avalanches when the activity goes above the threshold
# above_threshold = data > threshold_value
# avalanche_sizes = []
# current_size = 0

# # Calculate the size of each avalanche
# for point in range(len(above_threshold)):
#     if above_threshold[point]:
#         current_size += (order_parameter[point]-threshold_value)
#     else:
#         if current_size > 0:
#             avalanche_sizes.append(current_size)
#             current_size = 0

# # Add the last avalanche if it's not counted yet
# if current_size > 0:
#     avalanche_sizes.append(current_size)

# # Calculate the probability distribution
# sizes, counts = np.unique(avalanche_sizes, return_counts=True)
# probabilities = counts / counts.sum()

# # Plot the probability distribution on a log-log scale
# plt.loglog(sizes, probabilities, 'o')
# plt.xlabel('Avalanche Size (S)')
# plt.ylabel('Probability (P(S))')
# plt.title('Probability Distribution of Avalanche Sizes')
# plt.grid(True)
# plt.show()



#-------------------------------------------------------------------
# # Plot the evolution of neuron states
# plt.imshow(neuron_states, cmap='binary', interpolation='none')
# plt.xlabel('Time step')
# plt.ylabel('neuron State')
# plt.title('Neuron Activity Over Time')
# plt.colorbar(label='Active (1) / Inactive (0)')
# plt.show()




# # Set up the figure
# fig, ax = plt.subplots()
# cax = ax.matshow(neuron_states, cmap='viridis')

# def update(frame):

#     cax.set_array(neuron_states)
#     return cax,

# # Create the animation
# ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=200, blit=True)



# # Function to update the plot
# fig, ax = plt.subplots()
# line, = ax.plot([], [], lw=2)
# ax.set_ylim(0, 1)
# ax.set_xlim(0, time_steps)
# ax.set_xlabel("Time steps", size=12)
# ax.set_ylabel("Neuron Activation", size=12)
# ax.set_title("Activation of Neurons Over Time")

# x_data = np.arange(time_steps)


# def init():
#     line.set_data([], [])
#     return line,


# def animate(i):
#     y_data = neuron_states[:, i]
#     line.set_data(x_data, y_data)
#     return line,


# ani = animation.FuncAnimation(fig, animate, init_func=init, frames=time_steps, interval=50, blit=True)

# plt.show()




