public class Lab8Task1 {
	static void printReverse(int a[], int i) {
		if (i < 0)
			return;
		System.out.print(a[i] + " ");
		printReverse(a, i - 1);
	}

	static void printArrayAndReverse(int a[], int i) {
		if (i == a.length) {
			printReverse(a, a.length - 1);
			return;
		}
		System.out.print(a[i] + " ");
		printArrayAndReverse(a, i + 1);
	}

	public static void main(String[] args) {
		int arr[] = { 1, 3, 4, 7 };
		System.out.print("printReverse: ");
		printReverse(arr, arr.length - 1);
		System.out.print("\nprintArrayAndReverse: ");
		printArrayAndReverse(arr, 0);
	}
}