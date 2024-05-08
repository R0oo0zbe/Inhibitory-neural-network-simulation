## Understanding the Role of Inhibitory Neurons in the Neural Network Dynamics

The ceaseless dynamics introduced by inhibitory neurons are essential for the brain's ability to process information, maintain flexibility, and adapt to new situations. The study by Larremore et al. highlights the significance of these dynamics, showing that without inhibition, networks of excitable nodes would not exhibit behaviors necessary for normal brain function.

To delve into this further, we initiated our exploration by simulating a model of a neural network comprising 10,000 nodes, with only twenty percent of them functioning as inhibitors (reflecting the fraction of inhibitory neurons in the mammalian cortex). 

In our model, each node can exist in one of two states at each discrete time step $s_m(t) = 0$ or $s_m(t) = 1$. When a node $m$ is in the active state $s_m(t) = 1$, it sends an input of strength $A_{nm}$ to node $n$, whereas, in the inactive state $s_m(t) = 0$, no input is sent. 

Nodes are categorized as either excitatory or inhibitory, corresponding to $A_{nm} \ge 0$ or $A_{nm} \leq 0$, respectively, for all $n$. If there is no connection from node $n$ to node $m$, then $A_{nm} = 0$. 

At each time step $t$, each node $n$ computes the weighted sum of its inputs and passes the result through a transfer function $\sigma(\cdot)$. This process determines the node’s state at the next time step $t+1$ according to the equation:

![equations](https://latex.codecogs.com/svg.image?{\color{White}\[s_n(t&plus;1)=1\text{with&space;probability&space;of}\sigma\left(\sum_{m=1}^{N}A_{nm}s_m(t)\right)\]})

It's important to note that $\sigma(x) = 1$ for $x \geq 1$, $\sigma(x) = 0$ for $x \leq 0$, and $\sigma(x) = x$ for $0 < x < 1$. In the presence of excitatory inputs, the selected node may become active; however, in the absence of them, or in other words, the presence of net inhibitory input, it remains inactive.

The probability that each node $m$ connects to node $n$ is $p$. In a network of $N$ nodes, the mean of in-degree and out-degree is $\langle k \rangle = Np$. Initially, to construct the matrix $A$, each non-zero connection strength $A_{nm}$ is independently drawn from a distribution of positive numbers. While our analytical findings apply to any distribution with mean $\gamma$, in our simulations, we assume a uniform distribution on the interval $[0, 2\gamma]$. Additionally, a fraction of the nodes is designated as inhibitory, and each column of $A$ corresponding to the outgoing connections of an inhibitory node is multiplied by $-1$.

Previous studies have demonstrated that the dynamics of excitable networks are well-characterized by the largest eigenvalue of the network adjacency matrix $A$, with critical behavior occurring at $\lambda = 1$. To achieve a specific eigenvalue $\lambda$, we use the relation $\gamma = \lambda / [\langle k \rangle (1-2)]$, which serves as an accurate approximation for large networks. Also, previous studies cover a range of $0 \leq \alpha \leq 0.3$, including the fraction $\alpha \approx 0.2$, which corresponds to the proportion of inhibitory neurons in the mammalian cortex.

## How to Install and Work with the Simulation

These are the steps to run the program:

1) The user at the first step should set the [configuration](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/configuration.txt) that in this file **number_ nodes**, **number_active_nodes** are the total number of neural cells and the total neural cells that are activated in the initial time step ($t_0$). Also, **alfa** is the ratio of the inhibitor neural cells, and **probability_connection** is the probability that two nodes will be connected. It is worth mentioning that **landa** is an equivalent name to $\lambda$ which is the biggest eigenvalue of the adjacency matrix of the network (because lambda is a known function for Python we named it landa). In the end, **time_steps** and seed are the total number of time steps that the user wants to run the simulation and the seed value is the starting point for the sequence of random numbers.
2) To initiate the model, the user should execute the [simulation](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/simulation.py) file, which imports its parameters from the [configuration](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/configuration.txt) with using the ConfigParser library and in the end the result will be a plot that shows behavior of the system.

This project is divided into the following parts:

- [Functions](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/Functions.py#L7) collectively facilitate the simulation and analysis of neural networks. **'average_connection'** calculates the expected number of connections in the network based on node count and connection probability. **'sigma'** computes a parameter reflecting the balance between excitation and inhibition. **'create_matrix'** generates a connectivity matrix with randomly assigned connection strengths, incorporating inhibitory nodes. **'initial_state'** sets up the initial activation states of nodes. 'multiply' computes the next state of nodes by multiplying the current state with the connectivity matrix. Finally, **'plot'** visualizes the evolution of an order parameter over time, crucial for understanding network synchronization. Together, these functions offer a comprehensive toolkit for modeling and analyzing neural network dynamics.

- In the file [Test_Functions](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/Test_Functions.py) all the functions were tested  to ensure that all of them work properly. These tests aim to ensure that various functions within a neural network simulation behave as expected, using the Hypothesis library to generate diverse input scenarios. The `test_average_connection` function checks if the `average_connection` function accurately estimates the expected number of connections in the network based on the provided parameters. The `test_sigma` function verifies that the `sigma` function produces a valid result within a reasonable range. Similarly, the `test_create_matrix` function confirms that the `create_matrix` function generates a valid adjacency matrix with the correct dimensions. Lastly, the `test_initial_state` function examines if the `initial_state` function correctly initializes the activation states of nodes, ensuring that the total number of active nodes matches the specified number. These tests collectively validate the functionality and reliability of the neural network simulation code.

- In [simulation](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/simulation.py), a simulation of a neural network model is conducted, with parameters extracted from a [configuration](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/configuration.txt) file. Using a special module called [Functions](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/Functions.py#L7), important tasks for simulating networks are carried out. Over many turns, node activity changes based on how likely they are to get active, making the simulation run for a while. Lastly, a picture of how the network syncs up over time is made using the plot function.





