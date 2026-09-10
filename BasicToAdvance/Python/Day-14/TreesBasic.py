def preorder(root):
    # base case
    if root is None:
        return
    # visit root
    print(root.val)
    # left
    preorder(root.left)
    # right
    preorder(root.right)