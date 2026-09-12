# Level Order Traversal (BFS) of Binary Tree

from collections import deque

def level_traversal(root):

    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
