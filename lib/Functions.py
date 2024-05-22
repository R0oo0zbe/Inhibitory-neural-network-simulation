# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:56:28 2024

@author: Roozbe
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import configparser



def average_connection(number_nodes: int, probability: float) -> float:
    """ 
    This function multiplies the total number of neural cells and the probability of
    the connection between two cells to reach the average connectivity of each node.
    
    Parameters:
        number_nodes (int): Total number of neural cells.
        probability (float): Probability of the connection between two cells.
    
    Returns:
        float: The average connectivity of each node.
    """
    AverageConnection = number_nodes * probability
    return AverageConnection



def sigma(landa: float, alfa: float, AverageConnection: int) -> float:
    """ 
    This function will calculate the sigma with respect to the lambda formula that is 
    explained in the ReadMe part.
    
    Parameters:
        landa : float
            Lambda that is the largest eigenvalue of the adjacency matrix.
        alfa : float
            Ratio of the inhibitor nodes.
        AverageConnection : float
            Average connectivity of each node.
    
    Returns:
        float
            The sigma with respect to the formula.
    """
    numerator = landa
    denominator = AverageConnection * ( 1 - 2*alfa )
    sigma = np.divide( numerator, denominator)
    return sigma


def create_matrix(number_nodes: int, sigma: float, probability: float, alfa: float):
    """ 
    This function will create an adjacency matrix for the neural cells network.
    
    Parameters:
        number_nodes : int
            Total number of neural cells.
        sigma : float
            The sigma is the mean weight of the adjacency matrix.
        probability : float
            Probability of the connection between two cells.
        alfa : float
            Ratio of the inhibitor nodes.

    Returns:
        np.ndarray
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

def initial_state(number_nodes: int, number_active_nodes: int):
    """ 
    This function will create a list with N (total number of neural cells) values
    that values are 0 or 1 this list will be used for the initial state of the neuron cells.
    
    Parameters:
        number_nodes : int
            Total number of neural cells.
        number_active_nodes : int
            The number of nodes that are activated in the first time step (their value is 1).
    
    Returns:
        numpy.ndarray
            A list with N (total number of neural cells) values that values are 0 or 1.
    """
    initial_states = np.zeros(number_nodes)
    initial_states[:number_active_nodes] = 1
    return initial_states

def multiply(matrix, node_list):
    """ 
    This function will do a vector-matrix product.
    
    Parameters:
        matrix : numpy.ndarray
            Adjacency matrix of the network.
        node_list : list 
            The list of neural cells state.
    
    Returns:
        list
            A list with N (total number of neural cells) values between 0 and 1.
    """
    
  matrix = np.array(matrix)
  node_list = np.array(node_list)
  product_list = np.dot(node_list, matrix) 
  return product_list


def plot(order_parameter_list, number_nodes, alfa, landa, seed, probability):
    """ 
    This function will plot the behavior of the network.
    
    Parameters:
        order_parameter_list : list
            A list with the size of the total number of the time steps and each value shows how many nodes are active in that time step.
        number_nodes : int
            Total number of neural cells.
        alfa : float
            Ratio of the inhibitor nodes.
        landa : float
            Lambda that is the largest eigenvalue of the adjacency matrix.
        seed : int
            The seed value is the starting point for the sequence of random numbers.
        probability : float
            Probability of the connection between two cells.
    
    Shows:
        A plot that shows the behavior of the system (how many nodes are active in every time step).
    """
    
    config = configparser.ConfigParser()
    config.read('./configuration.txt')    
    landa = float(config.get('settings', 'landa'))
    destination1 = config.get('paths', 'critical_plot')
    destination2 = config.get('paths', 'subcritical_plot')
    destination3 = config.get('paths', 'supercritical_plot')
    plt.figure(figsize=(10, 6))
    plt.ylim(0, number_nodes)
    plt.plot(order_parameter_list, label="Order Parameter")
    plt.xlabel("Time steps", size=12)
    plt.ylabel("Order Parameter S", size=12)
    plt.title(r"$\lambda$={} and $\alpha$={}, seed={}, probability connection={}".format(landa, alfa, seed, probability))
    plt.legend()
    plt.grid(True)
    if landa == 1.0:
        plt.savefig(destination1)
    elif landa < 1.0:
        plt.savefig(destination2)
    else:
        plt.savefig(destination3)
    plt.show()

