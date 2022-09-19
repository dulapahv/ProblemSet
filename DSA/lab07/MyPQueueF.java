public class MyPQueueF {
	FibonacciMinPQ<Integer> heap = new FibonacciMinPQ<Integer>();

	public void enqueue(int d) {
		heap.insert(d);
	}

	public int dequeue() {
		return heap.delMin();
	}

	public int front() {
		return heap.minKey();
	}

	public boolean isEmpty() {
		return heap.isEmpty();
	}

	public String toString() {
		return heap.toString();
	}
}
