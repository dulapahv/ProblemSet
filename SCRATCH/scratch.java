// // public class scratch {
// // 	// public static void main(String[] args) {
// // 	// 	System.out.println("Hello World");
// // 	// }
// // 	static boolean isPrime0(int n) {
// // 		if (n==1) return false;
// // 		if (n<=3) return true;
// // 		int m = n/2;
// // 		for (int i = 2; i <= m; i++)
// // 			if (n % i == 0) return false;
// // 		return true;
// // 	}

// // 	public static void main(String[] args) {
// // 		int count = 0;
// // 		int N = 100000;
// // 		for (int n = 1; n < N; n++) {
// // 			if (isPrime0(n)) count++;
// // 		}
// // 		System.out.println("Pi(" + N + ")=" + count);
// // 	}
// // }

// // public class scratch {
// // 	static boolean isPrime0(int n) {
// // 		if (n==1) return false;
// // 		if (n<=3) return true;
// // 		int m = n/2;
// // 		for (int i = 2; i <= m; i++)
// // 			if (n % i == 0) return false;
// // 		return true;
// // 	}
// // }

// public class scratch {
// 	public static void main(String[] args) {
// 		int[] arr = {1, 2, 3, 4, 5, 6, 7, 8};
		
// 		MyLinkedList list = new MyLinkedList();
// 		for (int i = 0; i < arr.length; i++) {
// 			list.add(arr[i]);
// 		}
// 	}

// 	public void equal (MyLinkedList list, int[] arr) {
// 		for (int i = 0; i < arr.length; i++) {
// 			while (list != null) {
// 				if (list.data == arr[i]) {
// 					System.out.println(arr[i] + " ");
// 					break;
// 				}
// 				list = list.next;
// 			}
// 		}
// 	}
// }


public class scratch {
	public static void main(String[] args) {
		Double pickle = 2.0;
		int pickleInt = pickle.intValue();
		System.out.println(pickleInt);
	}
}