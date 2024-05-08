# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:56:28 2024

@author: Roozbe
"""
import numpy as np
import matplotlib.pyplot as plt
import random


def average_connection(number_nodes, probability):
    AverageConnection = np.multiply( number_nodes, probability)
    return AverageConnection

def sigma(landa, alfa, AverageConnection):
    numerator = landa
    denominator = AverageConnection * ( 1 - 2*alfa )
    sigma = np.divide( numerator, denominator)
    return sigma

def create_matrix(number_nodes, sigma, probability, alfa):
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
    initial_states = np.zeros(number_nodes)
    initial_states[:number_active_nodes] = 1
    return initial_states

def multiply(matrix, node_list):
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
















