class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class Kth_Smallest {

    static int count = 0;

    public static Integer kthSmallest(TreeNode root, int k) {
        return inorder(root, k);
    }

    public static Integer inorder(TreeNode node, int k) {

        if (node == null) {
            return null;
        }

        // 1. Search left subtree
        Integer left = inorder(node.left, k);

        // 2. If answer already found, stop
        if (left != null) {
            return left;
        }

        // 3. Visit current node
        count++;

        // 4. Check if this is kth node
        if (count == k) {
            return node.val;
        }

        // 5. Search right subtree
        return inorder(node.right, k);
    }

    public static void main(String[] args) {

        // Create BST
        TreeNode root = new TreeNode(50);

        root.left = new TreeNode(30);
        root.right = new TreeNode(70);

        root.left.left = new TreeNode(20);
        root.left.right = new TreeNode(40);

        root.right.left = new TreeNode(60);
        root.right.right = new TreeNode(80);

        // Find 3rd smallest
        int k = 3;

        count = 0;

        Integer answer = kthSmallest(root, k);

        System.out.println("K-th smallest: " + answer);
    }
}