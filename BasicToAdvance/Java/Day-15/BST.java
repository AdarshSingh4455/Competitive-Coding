public class BST {
    static class TreeNode{
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode (int val){
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }

    static TreeNode insertion(TreeNode root, int value){
        if (root == null) {
            return new TreeNode(value);
        }
        if (root.val > value) {    
            root.left = insertion(root.left, value);
        }else if (root.val < value) {
            root.right = insertion(root.right, value);
        }else{
            return root;
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
        root.left = new TreeNode(40);
        root.left.left = new TreeNode(30);
        root.right = new TreeNode(60);

        root = insertion(root, 70);
        inorder(root);
        System.out.println();
    }
}
