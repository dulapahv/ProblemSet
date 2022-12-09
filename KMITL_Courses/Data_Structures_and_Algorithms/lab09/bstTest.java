public class bstTest {
	public static void main(String[] args) {
		final int N = Integer.parseInt(args[0]);

		BinarySearchTree bst = new BinarySearchTree();

		long start1 = System.currentTimeMillis();
		for (int i = 1; i < N; i++) {
			bst.insert(i, bst.root);
		}
		long end1 = System.currentTimeMillis();
		System.out.println("First set of data: Time to add " + N + " elements: " + (end1 - start1) + " ms");

		bst = new BinarySearchTree();
		long start2 = System.currentTimeMillis();
		for (int i = 1; i < N; i++) {
			bst.insert((int) (N * Math.random()), bst.root);
		}
		long end2 = System.currentTimeMillis();
		System.out.println("Second set of data: Time to add " + N + " elements: " + (end2 - start2) + " ms");
	}
}
