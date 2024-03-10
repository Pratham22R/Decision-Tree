#Creates a new node.
#Checks if the node meets any stopping criteria, such as purity, maximum depth, or minimum information gain.
#If a stopping criterion is met, returns the node as a leaf node and stops further splitting.
#If no stopping criterion is met, calculates information gain for all features at the current node and selects the highest.
#Splits the dataset at the current node using the selected feature by creating two new nodes: left and right.
#Repeats steps 2 to 6 for each new node created after the split.