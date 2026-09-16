# Binary Search Tree: Insert a Node

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value), True

    if root.val > value:
        root.left, inserted = insert(root.left, value)

    elif root.val < value:
        root.right, inserted = insert(root.right, value)

    else:
        return root, False

    return root, inserted

root = TreeNode(50)
root.left = TreeNode(30)
root.left.right = TreeNode(40)
root.left.left = TreeNode(20)
root.right = TreeNode(70)
root.right.right = TreeNode(80)

value = int(input("Enter a node to insert in the tree: "))

_, inserted = insert(root, value)

if inserted:
    print(f"Value {value} inserted in BST!")
else:
    print(f"Value {value} already present in BST!")