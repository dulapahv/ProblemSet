public class MyLinkedList {
	public class Node {
		int data;
		Node next;

		public Node(int d) {
			this.data = d;
		}
	}

	Node head = null;

	public void add(int d) {
		Node p = new Node(d);
		p.next = head;
		head = p;
	}

	public void insert(int d) {
		Node p = new Node(d);
		Node q = head;
		while (q.next != null && q.next.data < d) {
			q = q.next;
		}
		p.next = q.next;
		q.next = p;
	}

	public Node find(int d) {
		Node p = head;
		while (p != null) {
			if (p.data == d)
				return p;
			p = p.next;
		}
		return null;
	}

	public void delete(int d) {
		Node t = new Node(d + 1);
		t.next = head;
		Node p = t;
		while ((p.next != null) && (p.next.data == d)) {
			p = p.next;
		}
		if (p.next != null) {
			p.next = p.next.next;
		}
		head = t.next;
	}

	public String toString() {
		StringBuffer sb = new StringBuffer("head ");
		Node p = head;
		while (p != null) {
			sb.append("--> [");
			sb.append(p.data);
			sb.append("]");
			p = p.next;
		}
		sb.append("-> null");
		return new String(sb);
	}
}