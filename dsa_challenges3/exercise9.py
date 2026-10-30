class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    # Helper function that passes down dynamic min/max boundary constraints
    def validate(node, low=float('-inf'), high=float('inf')):
        # An empty tree/node is valid by default
        if not node:
            return True
            
        # The current node's value must strictly fall within its allowed bounds
        if not (low < node.val < high):
            return False
            
        # Left child: Must be less than current node value (updates upper bound)
        # Right child: Must be greater than current node value (updates lower bound)
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))

    return validate(root)

