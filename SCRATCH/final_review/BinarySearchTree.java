public class BinarySearchTree {

    class TreeNode {
        int data;
        TreeNode left = null, right = null, parent = null;

        public TreeNode(int d) {
            data = d;
        }
    }

    TreeNode root = null;

    void insert(int d, TreeNode node) {
        if (node == null) {
            root = new TreeNode(d);
            System.out.println("Root node: " + root.data);
            return;
        }
        if (d < node.data) {
            if (node.left == null) {
                node.left = new TreeNode(d);
                node.left.parent = node;
                System.out.println("Left node: " + node.left.data);
            } else {
                insert(d, node.left);
            }
        } else {
            if (node.right == null) {
                node.right = new TreeNode(d);
                node.right.parent = node;
                System.out.println("Right node: " + node.right.data);
            } else {
                insert(d, node.right);
            }
        }
    }

    void printPreOrder(TreeNode node) {
        if (node == null)
            return;
        System.out.println(node.data + " ");
        printPreOrder(node.left);
        printPreOrder(node.right);
    }

    void printInOrder(TreeNode node) {
        if (node == null)
            return;
        printInOrder(node.left);
        System.out.println(node.data + " ");
        printInOrder(node.right);
    }

    void printPostOrder(TreeNode node) {
        if (node == null)
            return;
        printPostOrder(node.left);
        printPostOrder(node.right);
        System.out.println(node.data + " ");
    }

    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();

        bst.insert(0, bst.root);
        bst.insert(3, bst.root);
        bst.insert(1, bst.root);
        bst.insert(2, bst.root);
        
        System.out.println("Print In Order");
        bst.printInOrder(bst.root);
        System.out.println("Print Post Order");
        bst.printPostOrder(bst.root);
        System.out.println("Print Pre Order");
        bst.printPreOrder(bst.root);
    }
}
