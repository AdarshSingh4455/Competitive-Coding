public class BSTDeletion {
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }
    }

    static TreeNode findMin(TreeNode root) {
        while (root.left != null) {
            root = root.left;
        }
        return root;
    }

    static TreeNode delete(TreeNode root, int key) {
        if (root == null) {
            return null;
        }

        if (key < root.val) {
            root.left = delete(root.left, key);
        } else if (key > root.val) {
            root.right = delete(root.right, key);
        } else {
            // Case 1: no children
            if (root.left == null && root.right == null) {
                return null;
            }

            // Case 2: one child (right child)
            if (root.left == null) {
                return root.right;
            }

            // Case 2: one child (left child)
            if (root.right == null) {
                return root.left;
            }

            // Case 3: two children
            TreeNode successor = findMin(root.right);
            root.val = successor.val;
            root.right = delete(root.right, successor.val);
        }

        return root;
    }

    static void inorder(TreeNode root) {
        if (root == null) {
            return;
        }
        inorder(root.left);
        System.out.print(root.val + " ");
        inorder(root.right);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(50);
        root.left = new TreeNode(30);
        root.right = new TreeNode(70);
        root.left.left = new TreeNode(20);
        root.left.right = new TreeNode(40);
        root.right.left = new TreeNode(60);
        root.right.right = new TreeNode(80);

        System.out.println("Original BST:");
        inorder(root);
        System.out.println();

        int key = 30;
        root = delete(root, key);

        System.out.println("BST after deleting " + key + ":");
        inorder(root);
        System.out.println();
    }
}