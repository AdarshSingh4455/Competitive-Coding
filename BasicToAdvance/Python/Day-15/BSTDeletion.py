def find_min(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):

    # Tree/subtree empty
    if root is None:
        return None

    # Search left
    if key < root.val:
        root.left = delete(root.left, key)

    # Search right
    elif key > root.val:
        root.right = delete(root.right, key)

    # Node found
    else:

        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: Only right child
        if root.left is None:
            return root.right

        # Case 2: Only left child
        if root.right is None:
            return root.left

        # Case 3: Two children
        successor = find_min(root.right)

        root.val = successor.val

        root.right = delete(root.right, successor.val)

    return root