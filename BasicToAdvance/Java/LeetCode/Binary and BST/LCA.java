// public class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;

//     TreeNode() {}

//     TreeNode(int val) {
//         this.val = val;
//     }

//     TreeNode(int val, TreeNode left, TreeNode right) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
// }

public class LCA {
    static class TreeNode {
        int val;
        TreeNode right;
        TreeNode left;

        TreeNode(int val) {
            this.val = val;
        }
    }
    public static void main(String[] args) {
        TreeNode root = new TreeNode(6);
        root.left = new TreeNode(2);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(0);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(7);
        root.right.right = new TreeNode(9);

        LCA obj = new LCA();

        System.out.println("BST LCA (2, 8) = " + obj.find_lca(root, 2, 8).val);
        System.out.println("BST LCA (4, 9) = " + obj.find_lca(root, 4, 9).val);

        TreeNode root2 = new TreeNode(3);
        root2.left = new TreeNode(5);
        root2.right = new TreeNode(1);
        root2.left.left = new TreeNode(6);
        root2.left.right = new TreeNode(2);
        root2.right.left = new TreeNode(0);
        root2.right.right = new TreeNode(8);
        root2.left.right.left = new TreeNode(7);
        root2.left.right.right = new TreeNode(4);

        System.out.println("General tree LCA (5, 1) = " + obj.find_lca(root2, root2.left, root2.right).val);
    }

    // BST version: finds LCA using node values.
    public TreeNode find_lca(TreeNode root, int p, int q) {
        if (root == null) {
            return null;
        }

        if (p < root.val && q < root.val) {
            return find_lca(root.left, p, q);
        }

        if (p > root.val && q > root.val) {
            return find_lca(root.right, p, q);
        }

        return root;
    }

    // General binary tree version: finds LCA using node references.
    public TreeNode find_lca(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }

        TreeNode leftRes = find_lca(root.left, p, q);
        TreeNode rightRes = find_lca(root.right, p, q);

        if (leftRes != null && rightRes != null) {
            return root;
        }

        return leftRes != null ? leftRes : rightRes;
    }
}
