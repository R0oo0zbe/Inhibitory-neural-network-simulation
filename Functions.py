# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:56:28 2024

@author: Roozbe
"""
import numpy as np
import matplotlib.pyplot as plt
import random


def average_connection(number_nodes, probability):
        """ This function multiplies the total number of neural cells and the probability of
        the connection between two cells to reach the average connectivity of each node.
       
    Parameters
        number_nodes : Total number of neural cells.
        probability : Probability of the connection between two cells.
    
    Returns:
        The average connectivity of each node is an integer number.
       """
    AverageConnection = np.multiply( number_nodes, probability)
    return AverageConnection

def sigma(landa, alfa, AverageConnection):
            """ This function will calculate the sigma with respect to the lambda formula that is 
            explained in the ReadMe part.
       
    Parameters
        landa : Lambda that is the largest eigenvalue of the adjacency matrix.
        alfa : Ratio of the inhibitor nodes.
        AverageConnection : average connectivity of each node.
    Returns:
        The sigma with respect to the formula is a float number.
         """
    numerator = landa
    denominator = AverageConnection * ( 1 - 2*alfa )
    sigma = np.divide( numerator, denominator)
    return sigma

def create_matrix(number_nodes, sigma, probability, alfa):
            """ This function will create an adjacency matrix for the neural cells network.
       
            Parameters
                number_nodes : Total number of neural cells.
                sigma : The sigma is the mean weight of the adjacency matrix.
                probability : Probability of the connection between two cells.
                alfa : Ratio of the inhibitor nodes.

            Returns:
                The N*N (N is the total number of neural cells) matrix with a mean weight of sigma.
         """
    matrix = np.zeros((number_nodes, number_nodes))
    for i in range(number_nodes):
        for j in range( number_nodes):
            if random.random() < probability:
                strength = random.uniform(0, 2 * sigma)
                matrix[i][j] = strength
    inhibitory_nodes = random.sample(range(number_nodes), int(alfa * number_nodes))
    matrix[:, inhibitory_nodes] *= -1
    matrix=np.transpose(matrix)
    return matrix

def initial_state(number_nodes, number_active_nodes):
        """ This function will create a list with N (total number of neural cells) values
        that values are 0 or 1 this list will be used for the initial state of the neuron cells.
       
    Parameters
        number_nodes : Total number of neural cells.
        number_active_nodes : the number of nodes that are activated in the first time step (their value is 1).
    
    Returns:
        A list with N (total number of neural cells) values that values are 0 or 1.
       """
    initial_states = np.zeros(number_nodes)
    initial_states[:number_active_nodes] = 1
    return initial_states

def multiply(matrix, node_list):
        """ This function will do vector product.
       
    Parameters
        matrix : Adjacency matrix of the network.
        number_active_nodes : The list of neural cells state.
    
    Returns:
        A list with N (total number of neural cells) values is between 0 and 1.
       """
  matrix = np.array(matrix)
  node_list = np.array(node_list)
  product_list = np.dot(node_list, matrix) 
  return product_list

def plot(order_parameter_list, number_nodes, alfa, landa, seed, probability):
    plt.ylim(0,number_nodes)
    plt.plot(order_parameter_list)
    plt.xlabel("Time steps", size=12)
    plt.ylabel("Order Parameter S", size=12)
    plt.title(r"$\lambda$={} and $\alpha$={}, seed={}, probability connection={}".format(landa, alfa, seed, probability))
    plt.show()
















