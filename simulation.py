# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:58:48 2024

@author: Roozbe
"""

import configparser
import random
import Functions as func

config = configparser.ConfigParser()
config.read( 'configuration.txt')

number_nodes = int(config.get('settings', 'number_nodes'))
number_active_nodes = int(config.get('settings', 'number_active_nodes'))
alfa = float(config.get('settings', 'alfa'))
probability_connection = float(config.get('settings', 'probability_connection'))
time_steps = int(config.get('settings', 'time_steps'))
landa = float(config.get('settings', 'landa'))
seed = int(config.get('settings', 'seed'))

random.seed(seed)

average_connection = func.average_connection( number_nodes, probability_connection)
sigma= func.sigma( landa, alfa, average_connection)
adjacency_matrix = func.create_matrix ( number_nodes, sigma, probability_connection, alfa)
memory_nodes = func.initial_state ( number_nodes, number_active_nodes)


order_parameter=[] 
for j in range (time_steps):
    probability_list = func.multiply ( adjacency_matrix, memory_nodes)
    for i in range (number_nodes):
        if probability_list[i] >= random.random():
            memory_nodes[i] = 1
        else:
            memory_nodes[i] = 0
    sum_memory_nodes = sum(memory_nodes)            
    order_parameter.append(sum_memory_nodes) 
    
func.plot (order_parameter, number_nodes, alfa, landa, seed, probability_connection)














