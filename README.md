# Understanding the Role of Inhibitory Neurons in Neural Network Dynamics

The ceaseless dynamics introduced by inhibitory neurons are essential for the brain's ability to process information, maintain flexibility, and adapt to new situations. The study by Larremore et al. highlights the significance of these dynamics, showing that without inhibition, networks of excitable nodes would not exhibit behaviors necessary for normal brain function.

To delve into this further, we initiated our exploration by simulating a model of a neural network comprising 10,000 nodes, with only twenty percent of them functioning as inhibitors (reflecting the fraction of inhibitory neurons in the mammalian cortex). 

In our model, each node can exist in one of two states at each discrete time step $\( t \): \( s_m(t) = 0 \)$ or $\( s_m(t) = 1 \)$. When a node \( m \) is in the active state \( s_m(t) = 1 \), it sends an input of strength \( A_{nm} \) to node \( n \), whereas in the inactive state \( s_m(t) = 0 \), no input is sent. 

Nodes are categorized as either excitatory or inhibitory, corresponding to \( A_{nm} \geq 0 \) or \( A_{nm} \leq 0 \), respectively, for all \( n \). If there is no connection from node \( n \) to node \( m \), then \( A_{nm} = 0 \). 

At each time step \( t \), each node \( n \) computes the weighted sum of its inputs and passes the result through a transfer function \( \sigma(\cdot) \). This process determines the node’s state at the next time step \( (t+1) \) according to the equation:

\[ s_n(t + 1) = 1 \text{ with probability } \sigma\left( \sum_{m=1}^{N} A_{nm} s_m(t) \right) \]
