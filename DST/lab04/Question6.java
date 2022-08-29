public class Question6 extends MyLinkedList {
	public int getMiddle() {
		int size = 0;
		Node p = head;
		while (p != null) {
			size++;
			p = p.next;
		}
		int middle = size / 2;
		p = head;
		for (int i = 0; i < middle; i++) {
			p = p.next;
		}
		return p.data;
	}

	public static void main(String[] args) {
		Question6 mList = new Question6();
		mList.add(5);
		mList.add(4);
		mList.add(3);
		mList.add(2);
		mList.add(1);
		System.out.println(mList.toString());
		System.out.println(mList.getMiddle());
	}
}
