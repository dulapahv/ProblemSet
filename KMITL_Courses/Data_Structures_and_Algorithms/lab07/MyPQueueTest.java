public class MyPQueueTest {
	public static void main(String[] args) {
		MyPQueue q = new MyPQueue();
		MyPQueueTest test = new MyPQueueTest();
		test.test(q);
	}

	public void test(MyPQueue q) {
		q.enqueue(5);
		q.enqueue(3);
		q.enqueue(7);
		q.enqueue(1);
		q.enqueue(9);
		q.enqueue(2);
		q.enqueue(8);
		q.enqueue(4);
		q.enqueue(6);
		System.out.println(q);
		while (!q.isEmpty()) {
			System.out.println(q.dequeue());
		}
	}
}
