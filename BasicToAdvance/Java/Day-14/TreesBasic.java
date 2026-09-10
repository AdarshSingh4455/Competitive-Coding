public class TreesBasic {
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        
        TreeNode(int val) {
            this.val = val;
        }
    }
    
    public static void main(String[] args) {
    }
    void postorder(TreeNode root) {
        if (root == null) {
            return;
        }

        postorder(root.left);
        postorder(root.right);
        System.out.println(root.val);
    }

    void preOrder(TreeNode root){
        if (root==null){
            return;
        }

        System.out.println(root.val);
        preOrder(root.left);
        preOrder(root.right);
    }

    void InOrder(TreeNode root){
        if (root==null){
            return;
        }

        InOrder(root.left);
        System.out.println(root.val);
        InOrder(root.right);
    }
}