public class BinaryTree {
	class TreeNode {
		int data;
		TreeNode left, right;
	}

	TreeNode root = null;

	// TreeNode search(int d);
	// void insert(int d);
	// void delete(int d);
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
}