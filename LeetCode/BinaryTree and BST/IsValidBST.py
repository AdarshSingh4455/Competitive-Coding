class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    previous = None

    def inorder(node):
        nonlocal previous

        if node is None:
            return True

        if not inorder(node.left):
            return False

        if previous is not None and node.val <= previous:
            return False

        previous = node.val

        return inorder(node.right)

    return inorder(root)


if __name__ == "__main__":
    # Valid BST example
    root1 = TreeNode(5)
    root1.left = TreeNode(1)
    root1.right = TreeNode(8)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)

    # Invalid BST example
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)

    print("root1 is valid BST:", isValidBST(root1))
    print("root2 is valid BST:", isValidBST(root2))