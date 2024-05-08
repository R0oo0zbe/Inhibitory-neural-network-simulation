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

1) The user at the first step should set the [configuration](https://github.com/R0oo0zbe/Inhibitory-neural-network-simulation/blob/main/configuration.txt) that in this file $number_ nodes$, $number_ active_ nodes$ are the total number of neural cells and the total neural cells that are activated in the initial time step ($t_0$). Also, $alfa$ is the ratio of the inhibitor neural cells and $probability_ connection$ is the probability that two nodes will be connected. It is worth mentioning that $landa$ is an equivalent name to $\lambda$ which is the biggest eigenvalue of the adjacency matrix of the network (because lambda is a known function for Python we named it landa). In the end, $time_ steps$ and $seed$ are the total number of time steps that the user wants to run the simulation and the seed value is the starting point for the sequence of random numbers.








