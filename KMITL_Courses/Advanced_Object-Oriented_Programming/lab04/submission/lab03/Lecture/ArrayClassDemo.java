import java.util.Arrays;

public class ArrayClassDemo {
	public static void main(String[] args) {
		boolean areArraysEqual;
		// arrayA and arrayB
		int[] arrayA = { 5, 9, 1, 6 };
		int[] arrayB = { 5, 9, 1, 6 };
		System.out.println("arrayA contains " + Arrays.toString(arrayA));
		System.out.println("arrayB contains " + Arrays.toString(arrayB));
		areArraysEqual = arrayA.equals(arrayB); // test equality
		System.out.println("arrayA equals arrayB? " + areArraysEqual);
		// arrayA and arrayC
		int[] arrayC = arrayA;
		System.out.println("arrayC contains " + Arrays.toString(arrayA));
		areArraysEqual = arrayA.equals(arrayC); // test equality
		System.out.println("arrayA equals arrayC? " + areArraysEqual);
		// arrayA and arrayD
		int[] arrayD = new int[arrayA.length];
		System.arraycopy(arrayA, 0, arrayD, 0, arrayA.length);
		System.out.println("arrayD contains " + Arrays.toString(arrayD));
		areArraysEqual = arrayA.equals(arrayD); // test equality
		System.out.println("arrayA equals arrayD? " + areArraysEqual);
		// sort arrayA
		Arrays.sort(arrayA); // sort array in ascending order
		System.out.println("arrayA sorted is " + Arrays.toString(arrayA));
		// after sorting, search arrayA
		int value = 9;
		int position = Arrays.binarySearch(arrayA, value);
		System.out.println("The position of " + value + " in arrayA is " + position);
		// fill arrayA with zeros
		Arrays.fill(arrayA, 0);
		System.out.println("arrayA filled with 0s: " + Arrays.toString(arrayA));
	} // end main

}
