# Simulation of Neural network with Inhibitor Neural Cells
The concept of dynamic balance in the brain refers to the intricate equilibrium between excitatory and inhibitory signals that govern neural activity. This balance is crucial for the proper functioning of neural circuits and is involved in processes such as learning, memory, and overall brain plasticity. A pivotal aspect of this dynamic balance is the role of synaptic plasticity, which adjusts the strength of connections between neurons in response to activity. Synaptic plasticity is thought to be a fundamental mechanism underlying learning and memory. The study by Larremore et al. explores the paradoxical role of inhibitory nodes in networks of excitable nodes, revealing that instead of suppressing activity, they can sustain it. This concept comes from the dynamic balance in the brain, where a similar interplay between excitation and inhibition is crucial for healthy brain function.  The balance between excitation and inhibition is not static but is dynamically regulated by homeostatic mechanisms to maintain robust neural dynamics over long timescales. These mechanisms allow the brain to adapt to large perturbations, such as those caused by learning, aging, development, and certain diseases. By dynamically rebalancing brain networks, homeostatic mechanisms ensure that the brain remains functionally stable despite ongoing changes. Excitatory neurons transmit information, while inhibitory interneurons release neurotransmitters to reduce neuronal excitability and maintain neural network balance through interaction and restriction. This delicate balance is crucial for neurological health, as evidenced by observations linking Parkinson's disease and focal seizures to dynamic changes in excitatory and inhibitory connection strength in the basal ganglia. Studies have investigated these phenomena within the framework of excitatory-inhibitory balanced networks, highlighting the importance of maintaining this equilibrium for neural rhythm and function. Understanding the role of inhibitory synaptic plasticity in these mechanisms is vital for elucidating the pathophysiology of neurodegenerative diseases and developing potential therapeutic interventions. The ceaseless dynamics introduced by inhibitory neurons are essential for the brain's ability to process information, maintain flexibility, and adapt to new situations. The study by Larremore et al. highlights the significance of these dynamics, showing that without inhibition, networks of excitable nodes would not exhibit behaviors necessary for normal brain function. For the starting point, we simulated a model of a neural network with $10000$ nodes only twenty percent of them play inhibitor rull (corresponding to the fraction of inhibitory neurons in the mammalian cortex). The model represents at each discrete time step t, every node m can exist in one of two states: $s_m(t) = 0$ or $ s_m(t) = 1$. When a node m is in the active state $s_m(t) = 1$, a node $n$ receives an input of strength $A_{nm}$ , and when a node $m$ is in the inactive state $ s_m(t) = 0$. Each node m is categorized as either excitatory or inhibitory, corresponding to $A_{nm} \ge 0$ or  $A_{nm} \leq 0$  for all $n$  respectively. Also if there is no connection from a node $n$ to the node  $m$, then $A_{nm} = 0$. Each node  $n$ computes the weighted sum of its inputs at the time $t$ and passes the result through a transfer function $\sigma(\cdot)$. This process determines the node’s state at the time $(t+1)$: 

 $\[ s_n(t + 1) = 1  \text{ with probability of }  \sigma\left( \sum_{m=1}^{N} A_{nm} s_m(t) \right) \]   $
 
And 0 otherwise, $\sigma(x)=1$ for  $x \geq 1$, this function is equal to zero $( \sigma(x)=0 )$ for $ x \leq 0$ and $\sigma(x)=x$ for $0 <x <1$. It is worth mentioning that in the presence of excitatory inputs, the selected node may become active; however in the absence of them, or in other words the presence of net inhibitory input, it remains inactive. The probability that each node $m$ connects node $n$ is $p$. In a network of $N$ nodes, the mean of in-degree and out-degree is $ <k> =Np$. Initially, to construct the matrix $A$, each non-zero connection strength $A_{nm}$ is independently drawn from a distribution of positive numbers. While our analytical findings apply to any distribution with mean $\gamma$, in our simulations, we assume a uniform distribution on the interval $[0, 2\gamma]$. Additionally, a fraction of the nodes is designated as inhibitory, and each column of $A$ corresponding to the outgoing connections of an inhibitory node is multiplied by $-1$. Previous studies have demonstrated that the dynamics of excitable networks are well-characterized by the largest eigenvalue of the network adjacency matrix $A$, with critical behavior occurring at $\lambda=1$. To achieve a specific eigenvalue $\lambda$, we use the relation $\gamma=\lambda /[<k>(1-2)]$, which serves as an accurate approximation for large networks [7]. Our exploration covers a range of $0  \leq \alpha \leq 0.3$, including the fraction $\alpha \approx 0.2$, which corresponds to the proportion of inhibitory neurons in the mammalian cortex.
