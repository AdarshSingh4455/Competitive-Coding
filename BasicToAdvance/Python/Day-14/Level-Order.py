from collections import deque

def level_order(root):
    if root is None:
        return

    queue = deque([root])
    result = []

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            level.append(node.val)

            if root.left is None:
                queue.append(node.left)

            if root.right is None:
                queue.append(node.right)

        result.append(level)

    return result