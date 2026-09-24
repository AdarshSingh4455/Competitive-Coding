public class BSTPredecessor {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static Node findMax(Node root) {
        while (root.right != null) {
            root = root.right;
        }
        return root;
    }

    static Node predecessor(Node root, int key) {
        Node predecessor = null;

        while (root != null) {
            if (key > root.val) {
                predecessor = root;
                root = root.right;
            } else if (key < root.val) {
                root = root.left;
            } else {
                break;
            }
        }

        if (root != null && root.left != null) {
            return findMax(root.left);
        }

        return predecessor;
    }

    public static void main(String[] args) {
        Node root = new Node(50);
        root.left = new Node(30);
        root.right = new Node(70);
        root.left.left = new Node(20);
        root.left.right = new Node(40);
        root.right.left = new Node(60);
        root.right.right = new Node(80);

        int key = 60;
        Node result = predecessor(root, key);

        if (result != null) {
            System.out.println("Predecessor of " + key + " is " + result.val);
        } else {
            System.out.println("No predecessor exists for " + key);
        }
    }
}
