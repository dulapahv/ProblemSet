public class test {
	// Write a java method that takes an array and a linked list and print out the elements that appear in both array and linked list. 
	public static void printIntersection(MyLinkedList list, MyArray arr) {
		MyLinkedList.Node p = list.head;
		while (p != null) {
			if (arr.find(p.data) != -1) {
				System.out.print(p.data + " ");
			}
			p = p.next;
		}
	}

	public static void main(String[] args) {
		MyArray arr = new MyArray(10);
		arr.add(1);
		arr.add(2);
		arr.add(3);
		arr.add(5);
		arr.add(7);
		arr.add(9);
		MyLinkedList list = new MyLinkedList();
		list.add(3);
		list.add(4);
		list.add(6);
		list.add(7);
		list.add(8);

		printIntersection(list, arr);
	}
}
