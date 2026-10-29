def count_leaves(root):
    # Base Case 1: If the node is empty, it contributes 0 leaves
    if root is None:
        return 0
        
    # Base Case 2: If a node has no left and no right child, it is a leaf node!
    if root.left is None and root.right is None:
        return 1
        
    # Recursive Step: Count leaves in both subtrees and sum them up
    return count_leaves(root.left) + count_leaves(root.right)
