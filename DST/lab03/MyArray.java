public class MyArray {
	private int[] arr;
	private int size;
	private int MAX_SIZE = 5;

	MyArray() {
		this.arr = new int[MAX_SIZE];
	}

	public void add(int n) {
		if (!isFull()) {
			this.arr[this.size++] = n;
		} else
			this.expand();
	}

	public boolean isFull() {
		return this.size == MAX_SIZE;
	}

	public void expand() {
		MAX_SIZE = 2 * MAX_SIZE;
		int[] newArr = new int[MAX_SIZE];
		System.arraycopy(this.arr, 0, newArr, 0, size);
		this.arr = newArr;
	}

	public void insert(int n, int index) {
		for (int i = this.size; i > index; i--) {
			this.arr[i] = this.arr[i - 1];
		}
		this.arr[index] = n;
		this.size++;
	}

	public int find(int n) {
		for (int i = 0; i < this.size; i++) {
			if (this.arr[i] == n) {
				return i;
			}
		}
		return -1;
	}

	public int binarySearch(int n) {
		int a = 0, b = this.size - 1;
		while (a <= b) {
			int m = (a + b) / 2;
			if (this.arr[m] == n) {
				return m;
			}
			if (n < this.arr[m]) {
				b = m - 1;
			} else
				a = m + 1;
		}
		return -1;
	}

	public void deleteU(int index) {
		this.arr[index] = this.arr[--this.size];
	}

	public void deleteO(int index) {
		for (int i = index; i < this.size - 1; i++) {
			this.arr[i] = this.arr[i + 1];
		}
		this.size--;
	}
}