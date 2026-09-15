# Binary Search Tree (BST) - Search Operation
# Problem: Search for a target value in a Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search(root, target):
    current = root

    while current:
        if current.val == target:
            return True

        if current.val > target:
            current = current.left
        else:
            current = current.right

    return False

if __name__ == "__main__":
    # Create a sample BST
    #       5
    #      / \
    #     3   7
    #    / \ / \
    #   2  4 6  8
    
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    
    target = int(input("Enter the value to search in BST: "))

    result = search(root, target)
    
    if result:
        print(f"Value {target} found in BST!")
    else:
        print(f"Value {target} not found in BST!")
