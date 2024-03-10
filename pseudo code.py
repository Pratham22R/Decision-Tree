Creates a new node.
Checks if the node meets any stopping criteria, such as purity, maximum depth, or minimum information gain.
If a stopping criterion is met, returns the node as a leaf node and stops further splitting.
If no stopping criterion is met, calculates information gain for all features at the current node and selects the highest.
Splits the dataset at the current node using the selected feature by creating two new nodes: left and right.
Repeats steps 2 to 6 for each new node created after the split.

PSEUDO CODE

class TreeNode:
    def __init__(self, feature_index=None, threshold=None, value=None, left=None, right=None):
        self.feature_index = feature_index
        self.threshold = threshold
        self.value = value
        self.left = left
        self.right = right

def build_tree(X, y, max_depth):
    if len(set(y)) == 1 or max_depth == 0:
        return TreeNode(value=most_common_class(y))

    feature_index, threshold = find_best_split(X, y)
    X_left, y_left, X_right, y_right = split_data(X, y, feature_index, threshold)
    left_subtree = build_tree(X_left, y_left, max_depth - 1)
    right_subtree = build_tree(X_right, y_right, max_depth - 1)
    
    return TreeNode(feature_index=feature_index, threshold=threshold, left=left_subtree, right=right_subtree)

def find_best_split(X, y):
    best_feature_index = 0
    best_threshold = X[0][0]
    return best_feature_index, best_threshold

def split_data(X, y, feature_index, threshold):
    X_left = [sample for sample in X if sample[feature_index] < threshold]
    y_left = [y[i] for i in range(len(X)) if X[i][feature_index] < threshold]
    X_right = [sample for sample in X if sample[feature_index] >= threshold]
    y_right = [y[i] for i in range(len(X)) if X[i][feature_index] >= threshold]
    return X_left, y_left, X_right, y_right

def most_common_class(y):
    from statistics import mode
    return mode(y)

# Example usage
# decision_tree = build_tree(X_train, y_train, max_depth=3)

