class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)

    if root.val > value:
        root.left = insert(root.left, value)

    elif root.val < value:
        root.right = insert(root.right, value)

    else:
        return root

    return root

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

root = TreeNode(50)
root.left = TreeNode(30)
root.left.right = TreeNode(40)
root.left.left = TreeNode(20)
root.right = TreeNode(70)
root.right.right = TreeNode(80)

value = int(input("Enter a node to insert in the tree: "))

root = insert(root,value)

print(f"Value {value} inserted in BST!")

inorder(root)
