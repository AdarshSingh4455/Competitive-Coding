public class BinaryPreorder {
    static class TreeNode {
        int val;
        TreeNode right;
        TreeNode left;

        TreeNode(int val) {
            this.val = val;
        }
    }

    static void preOrder(TreeNode node, java.util.List<Integer> result) {
        if (node == null) {
            return;
        }

        result.add(node.val);
        preOrder(node.left, result);
        preOrder(node.right, result);
    }

    static int[] Binary_PreOrder(TreeNode root) {
        java.util.List<Integer> result = new java.util.ArrayList<>();
        preOrder(root, result);

        int[] ans = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            ans[i] = result.get(i);
        }
        return ans;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        int[] ans = Binary_PreOrder(root);
        for (int value : ans) {
            System.out.print(value + " ");
        }
    }
}
