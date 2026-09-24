# BST Predecessor

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_max(root):
    while root.right:
        root = root.right
    return root


def predecessor(root, key):
    predecessor = None

    while root:
        if key > root.val:
            predecessor = root
            root = root.right
        elif key < root.val:
            root = root.left
        else:
            break

    if root and root.left:
        return find_max(root.left)

    return predecessor


# Example usage
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)
print(predecessor(root, 60).val)  # Output: 50
print(predecessor(root, 30).val)  # Output: 20