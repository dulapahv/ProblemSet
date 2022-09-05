public class Question4 extends MyLinkedList {
	public void reverse() {
		Node prev = null;
		Node curr = head;
		Node next = null;
		while (curr != null) {
			next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}
		head = prev;
	}

	public static void main(String[] args) {
		Question4 mList = new Question4();
		mList.add(5);
		mList.add(4);
		mList.add(3);
		mList.add(2);
		mList.add(1);
		System.out.println(mList.toString());
		mList.reverse();
		System.out.println(mList.toString());
	}
}
