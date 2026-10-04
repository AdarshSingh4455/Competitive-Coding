class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_LCA(root, p, q):
    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left_res = find_LCA(root.left, p, q)
    right_res = find_LCA(root.right, p, q)

    if left_res is not None and right_res is not None:
        return root
    elif left_res is not None:
        return left_res
    elif right_res is not None:
        return right_res

    return None


def build_tree(values):
    if not values or values[0] == -1:
        return None

    root = Node(values[0])
    queue = [root]
    index = 1

    while queue and index < len(values):
        current = queue.pop(0)

        if index < len(values):
            left_val = values[index]
            index += 1
            if left_val != -1:
                current.left = Node(left_val)
                queue.append(current.left)

        if index < len(values):
            right_val = values[index]
            index += 1
            if right_val != -1:
                current.right = Node(right_val)
                queue.append(current.right)

    return root


def main():
    tree_input = input("Enter tree values in level-order format (-1 for empty nodes): ")
    if not tree_input.strip():
        print("No tree data entered.")
        return

    values = list(map(int, tree_input.split()))
    root = build_tree(values)

    p = int(input("Enter first node value: "))
    q = int(input("Enter second node value: "))

    lca = find_LCA(root, p, q)

    if lca is None:
        print(f"LCA of {p} and {q} is not found in the tree.")
    else:
        print(f"LCA of {p} and {q} is: {lca.val}")


if __name__ == "__main__":
    main()