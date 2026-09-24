# Search Kth Smallest Element in a BST

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def kth_smallest(root, k):
    count = 0

    def inorder(node):
        nonlocal count

        if node is None:
            return None

        # 1. Search left subtree
        left = inorder(node.left)

        # 2. If answer already found, stop
        if left is not None:
            return left

        # 3. Visit current node
        count += 1

        # 4. Check if this is kth node
        if count == k:
            return node.val

        # 5. Search right subtree
        return inorder(node.right)

    return inorder(root)


# Create BST
root = TreeNode(50)

root.left = TreeNode(30)
root.right = TreeNode(70)

root.left.left = TreeNode(20)
root.left.right = TreeNode(40)

root.right.left = TreeNode(60)
root.right.right = TreeNode(80)


# Find 3rd smallest
k = 3
answer = kth_smallest(root, k)

print("K-th smallest:", answer)