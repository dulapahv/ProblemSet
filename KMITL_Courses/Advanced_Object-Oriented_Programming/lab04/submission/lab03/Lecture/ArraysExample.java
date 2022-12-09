public class ArraysExample {
	public static void main(String[] args) {
		// TODO code application logic here
		int integerArray[];
		int[] alias;

		integerArray = new int[5];
		for (int index = 0; index < integerArray.length; index++) {
			integerArray[index] = 5;
		}

		alias = integerArray;
		alias[3] = 10;
		System.out.println(integerArray[3]);

		integerArray = new int[3];
		System.out.println(integerArray[3]);
		System.out.println(alias[3]);
	}

}
