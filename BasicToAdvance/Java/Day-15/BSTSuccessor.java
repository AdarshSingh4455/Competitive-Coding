// Find the inorder successor of a given key in a Binary Search Tree.

class BSTSuccessor {
    static class Node {
        int val;
        Node left;
        Node right;

        Node(int val) {
            this.val = val;
        }
    }

    static Node findMin(Node node) {
        while (node != null && node.left != null) {
            node = node.left;
        }
        return node;
    }

    static Node successor(Node root, int key) {
        Node successor = null;

        while (root != null) {
            if (key < root.val) {
                successor = root;
                root = root.left;
            } else if (key > root.val) {
                root = root.right;
            } else {
                break;
            }
        }

        if (root != null && root.right != null) {
            return findMin(root.right);
        }

        return successor;
    }

    public static void main(String[] args) {
        Node root = new Node(20);
        root.left = new Node(10);
        root.right = new Node(30);
        root.left.left = new Node(5);
        root.left.right = new Node(15);
        root.right.left = new Node(25);
        root.right.right = new Node(35);

        int key = 20;
        Node result = successor(root, key);

        if (result != null) {
            System.out.println("Successor of " + key + " is: " + result.val);
        } else {
            System.out.println("No successor exists for " + key);
        }
    }
}