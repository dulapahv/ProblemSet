public class MyArray {
	int[] arr;
	int size;
	int capacity;

	public MyArray(int capacity) {
		this.capacity = capacity;
		arr = new int[capacity];
		size = 0;
	}

	public void add(int d) {
		if (size == capacity) {
			capacity *= 2;
			int[] temp = new int[capacity];
			for (int i = 0; i < size; i++) {
				temp[i] = arr[i];
			}
			arr = temp;
		}
		arr[size++] = d;
	}

	public void insert(int d) {
		if (size == capacity) {
			capacity *= 2;
			int[] temp = new int[capacity];
			for (int i = 0; i < size; i++) {
				temp[i] = arr[i];
			}
			arr = temp;
		}
		int i = size - 1;
		while (i >= 0 && arr[i] > d) {
			arr[i + 1] = arr[i];
			i--;
		}
		arr[i + 1] = d;
		size++;
	}

	public int find(int d) {
		for (int i = 0; i < size; i++) {
			if (arr[i] == d)
				return i;
		}
		return -1;
	}

	public void delete(int d) {
		int i = find(d);
		if (i == -1)
			return;
		for (int j = i; j < size - 1; j++) {
			arr[j] = arr[j + 1];
		}
		size--;
	}

	public String toString() {
		StringBuffer sb = new StringBuffer();
		for (int i = 0; i < size; i++) {
			sb.append(arr[i]);
			sb.append(" ");
		}
		return sb.toString();
	}
}
