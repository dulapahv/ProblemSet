public class MyArray {
	private int MAX_SIZE = 1;
	private int[] array;

	public MyArray() {
		array = new int[1];
	}

	public MyArray(int[] array) {
		this.array = array;
	}

	private void expand() {
		MAX_SIZE *= 2;
		int[] temp = new int[MAX_SIZE * 2];
		System.arraycopy(array, 0, temp, 0, array.length);
		array = temp;
	}

	boolean isFull() {
		return array.length == MAX_SIZE;
	}

	boolean isEmpty() {
		return array.length == 0;
	}

	void add(int a) {
		if (array.length == MAX_SIZE) {
			expand();
		}
		array[array.length - 1] = a;
	}

	void insert(int a, int index) {
		int[] newArray = new int[array.length + 1];
		System.arraycopy(array, 0, newArray, 0, index);
		newArray[index] = a;
		System.arraycopy(array, index, newArray, index + 1, array.length - index);
		array = newArray;
	}

	int find(int a) {
		for (int i = 0; i < array.length; i++) {
			if (array[i] == a) {
				return i;
			}
		}
		return -1;
	}

	int binarySearch(int a) {
		int low = 0;
		int high = array.length - 1;
		while (low <= high) {
			int mid = (low + high) / 2;
			if (array[mid] == a) {
				return mid;
			} else if (array[mid] < a) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}
		return -1;
	}

	private void delete(int index) {
		int[] newArray = new int[array.length - 1];
		System.arraycopy(array, 0, newArray, 0, index);
		System.arraycopy(array, index + 1, newArray, index, array.length - index - 1);
		array = newArray;
	}

	void deleteUnordered(int a) {
		int index = find(a);
		if (index != -1) {
			delete(index);
		}
	}

	void deleteOrdered(int a) {
		int index = binarySearch(a);
		if (index != -1) {
			delete(index);
		}
	}

	public String toString() {
		String s = "";
		for (int i = 0; i < array.length; i++) {
			s += array[i] + ", ";
		}
		return s;
	}

	int getAt(int index) {
		return array[index];
	}

	void setAt(int index, int value) {
		array[index] = value;
	}

}