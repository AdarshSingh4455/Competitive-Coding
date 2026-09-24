class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_min(node):
    while node and node.left:
        node = node.left
    return node


def successor(root, key):
    succ = None
    curr = root

    while curr:
        if key < curr.val:
            succ = curr
            curr = curr.left
        elif key > curr.val:
            curr = curr.right
        else:
            if curr.right:
                return find_min(curr.right)
            break

    return succ


# Example usage
if __name__ == "__main__":
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.right.left = Node(25)
    root.right.right = Node(40)

    print(successor(root, 20))  # 25
    print(successor(root, 10))  # 15
    print(successor(root, 40))  # None
    print(successor(root, 5))   # 10