# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:39:20 2024

@author: Roozbe
"""
import numpy as np
import configparser
import Functions as func
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given

config = configparser.ConfigParser()
config.read( 'configuration.txt')

number_nodes = int(config.get('settings', 'number_nodes'))
number_active_nodes = int(config.get('settings', 'number_active_nodes'))
alfa = float(config.get('settings', 'alfa'))
probability_connection = float(config.get('settings', 'probability_connection'))
time_steps = int(config.get('settings', 'time_steps'))
landa = float(config.get('settings', 'landa'))



@given(st.integers(min_value=0, max_value=number_nodes), st.floats(min_value=0, max_value=probability_connection))
@settings(max_examples=1)
def test_average_connection(number_nodes, probability_connection):
        expected_result = number_nodes * probability_connection
        assert func.average_connection(number_nodes, probability_connection) == expected_result 
        
@given(st.floats(min_value=0, max_value=landa), st.floats(min_value=0, max_value=alfa))
@settings(max_examples=1)
def test_sigma(landa, alfa):
    average_connection = number_nodes * probability_connection
    result = func.sigma(landa, alfa, average_connection)
    assert np.isfinite(result)
    

@given(
    st.integers(min_value=0, max_value=number_nodes), 
    st.floats(min_value=0, max_value=landa),    
    st.floats(min_value=0, max_value=alfa)       
)
@settings(max_examples=1)
def test_create_matrix(number_nodes, landa, alfa):
    average_connection = number_nodes * probability_connection
    sigma = func.sigma(landa, alfa, average_connection)
    result = func.create_matrix(number_nodes, sigma, probability_connection, alfa)
    assert result.shape == (number_nodes, number_nodes)

@given(st.integers(min_value=10, max_value=number_nodes), st.integers(min_value=1, max_value=number_active_nodes))
@settings(max_examples=1)
def test_initial_state(number_nodes, number_active_nodes):
    results = func.initial_state(number_nodes, number_active_nodes)
    assert sum(results) == number_active_nodes
    

if __name__ == "__main__":
    test_average_connection()



