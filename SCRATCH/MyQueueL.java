public class MyQueueL {
	public static class Node {
		double data;
		Node next;

		public Node(double d) {
			data = d;
		}
	}

	Node head = null, tail;

	public void enqueue(double d) {
		Node p = new Node(d);
		if (head == null)
			head = tail = p;
		else {
			tail.next = p;
			tail = tail.next;
		}
	}

	public double dequeue() {
		double d = head.data;
		head = head.next;
		return d;
	}

	public double front() {
		return head.data;
	}

	public boolean isFull() {
		return false;
	}

	public boolean isEmpty() {
		return head == null;
	}

	public String toString() {
		String s = "";
		Node p = head;
		while (p != null) {
			s += p.data + " ";
			p = p.next;
		}
		return s;
	}
}
