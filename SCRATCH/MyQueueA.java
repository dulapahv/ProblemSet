public class MyQueueA {
	int MAX_SIZE = 100;
	String[] queue = new String[MAX_SIZE];
	int head = 0, tail = 0;

	public void enqueue(String d) {
		queue[tail] = d;
		tail = (tail + 1) % MAX_SIZE;
	}

	public String dequeue() {
		String d = queue[head];
		head = (head + 1) % MAX_SIZE;
		return d;
	}

	public String front() {
		return queue[head];
	}

	public boolean isFull() {
		return ((tail + 1) % MAX_SIZE) == head;
	}

	public boolean isEmpty() {
		return head == tail;
	}

	@Override
	public String toString() {
		String s = "";
		int i = head;
		while (i != tail) {
			s += queue[i] + " ";
			i = (i + 1) % MAX_SIZE;
		}
		return s;
	}
}
