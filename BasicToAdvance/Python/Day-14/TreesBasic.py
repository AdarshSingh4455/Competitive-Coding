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

def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)