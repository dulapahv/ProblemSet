public class BinarySearchTree {
	class TreeNode {
		int data;
		TreeNode left = null, right = null, parent = null;

		public TreeNode(int d) {
			data = d;
		}
	}

	TreeNode root = null;

	TreeNode search(int d, TreeNode node) {
		if (node == null)
			return null;
		if (d == node.data)
			return node;
		if (d < node.data)
			return search(d, node.left);
		return search(d, node.right);
	}

	void insert(int d, TreeNode node) {
		if (node == null) {
			root = new TreeNode(d);
			return;
		}
		if (d < node.data) {
			if (node.left == null) {
				node.left = new TreeNode(d);
				node.left.parent = node;
			} else
				insert(d, node.left);
		} else {
			if (node.right == null) {
				node.right = new TreeNode(d);
				node.right.parent = node;
			} else
				insert(d, node.right);
		}
	}

	void delete(int d, TreeNode node) {
		if (node == null)
			return;
		if (d < node.data)
			delete(d, node.left);
		else if (d > node.data)
			delete(d, node.right);
		else { // now, time to delete
			if ((node.left == null) || (node.right == null)) { // 0 or 1 child
				TreeNode q = (node.left == null) ? node.right : node.left;
				if (node.parent.left == node) // this node is a left child
					node.parent.left = q;
				else
					node.parent.right = q;
				if (q != null)
					q.parent = node.parent;
			} else { // 2 children
				TreeNode q = findMax(node.left);
				delete(q.data, node.left);
				if (node.parent.left == node)
					node.parent.left = q;
				else
					node.parent.right = q;
				q.left = node.left;
				q.right = node.right;
			}
		}
	}

	TreeNode findMax(TreeNode node) {
		if (node == null)
			return null;
		if (node.right == null)
			return node;
		return findMax(node.right);
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
}