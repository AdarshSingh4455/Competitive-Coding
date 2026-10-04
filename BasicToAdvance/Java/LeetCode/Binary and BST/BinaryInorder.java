public class BinaryInorder {
    static class TreeNode {
        int val;
        TreeNode right;
        TreeNode left;

        TreeNode(int val) {
            this.val = val;
        }
    }

    static void BinInorder(TreeNode node, java.util.List<Integer> result) {
        if (node == null) {
            return;
        }

        BinInorder(node.left, result);
        result.add(node.val);
        BinInorder(node.right, result);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        java.util.List<Integer> result = new java.util.ArrayList<>();
        BinInorder(root, result);

        System.out.println(result);
    }
}
