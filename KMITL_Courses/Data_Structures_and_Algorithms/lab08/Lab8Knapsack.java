public class Lab8Knapsack {

	public static int ans = 0;
	public static int[] indexList = new int[6];
	public static int indexListSize = 0;

	public static void main(String[] args) {
		int weight[] = { 1, 2, 3, 8, 7, 4 };
		int val[] = { 20, 5, 10, 50, 40, 25 };
		int w = 10;

		int curList[] = new int[6];
		int curListSize = 0;
		
		int minIndex = 0, maxIndex = 0;
		for (int i = 0; i < val.length; i++) {
			if (weight[i] < weight[minIndex]) {
				minIndex = i;
			}

			if (weight[i] > weight[maxIndex]) {
				maxIndex = i;
			}
		}
		knapsack(weight, val, w, 0, 0, 0, curList, curListSize, minIndex);
		knapsack(weight, val, w, 0, 0, 0, curList, curListSize, maxIndex);

		System.out.println("Knapsack value is " + ans);
		System.out.println("index: " + printList(indexList, indexListSize));
		System.out.print("value: ");
		for (int i = 0; i < indexListSize; i++) {
			System.out.print(val[indexList[i]] + " ");
		}

		System.out.println();
		System.out.print("weight: ");
		for (int i = 0; i < indexListSize; i++) {
			System.out.print(weight[indexList[i]] + " ");
		}
	}

	public static void knapsack(int weight[], int val[], int w, int i, int curWeight, int curVal,
			int curList[], int curListSize, int excludeIndex) {
		if (curVal > ans && curListSize % 2 == 0) {
			ans = curVal;
			indexListSize = 0;
			for (int j = 0; j < curListSize; j++) {
				indexList[indexListSize++] = curList[j];
			}
		}

		if (i == val.length) {
			return;
		}

		if (curWeight + weight[i] <= w && i != excludeIndex) {
			curList[curListSize++] = i;
			knapsack(weight, val, w, i + 1, curWeight + weight[i], curVal + val[i], curList, curListSize, excludeIndex);
			curListSize--;
			knapsack(weight, val, w, i + 1, curWeight, curVal, curList, curListSize, excludeIndex);
		} else {
			knapsack(weight, val, w, i + 1, curWeight, curVal, curList, curListSize, excludeIndex);
		}
	}

	public static String printList(int[] l, int size) {
		String s = "";
		for (int i = 0; i < size; i++) {
			s += l[i] + " ";
		}

		return s;
	}

}