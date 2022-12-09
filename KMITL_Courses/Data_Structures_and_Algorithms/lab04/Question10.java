public class Question10 extends MyLinkedList {
	public boolean isPalindrome() {
		Node slow = head;
		Node fast = head;
		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		Node secondHalf = slow.next;
		slow.next = null;
		Node prev = null;
		Node curr = secondHalf;
		Node next = null;
		while (curr != null) {
			next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}
		Node firstHalf = head;
		while (prev != null) {
			if (prev.data != firstHalf.data)
				return false;
			prev = prev.next;
			firstHalf = firstHalf.next;
		}
		return true;
	}

	public static void main(String[] args) {
		Question10 mList1 = new Question10();
		mList1.add(5);
		mList1.add(4);
		mList1.add(3);
		mList1.add(2);
		mList1.add(1);
		System.out.println(mList1.toString());
		System.out.println(mList1.isPalindrome());

		Question10 mList2 = new Question10();
		mList2.add(1);
		mList2.add(2);
		mList2.add(3);
		mList2.add(2);
		mList2.add(1);
		System.out.println(mList2.toString());
		System.out.println(mList2.isPalindrome());
	}
}