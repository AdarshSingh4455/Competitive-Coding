# Ques :- 94 ... Inorder traversal of Binary Tree.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result = []

        def postorder(node):
            if node is None:
                return

            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

        postorder(root)
        return result

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(Solution().postorderTraversal(root))