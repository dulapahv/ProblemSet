import java.util.Scanner;

public class CalculationAppC {
	public static void main(String[] args) {
		int x = 0, y = 0, z = 0;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter first integer: ");
		x = scan.nextInt();
		System.out.print("Enter second integer: ");
		y = scan.nextInt();
		System.out.print("Enter third integer: ");
		z = scan.nextInt();

		Calculation c = new Calculation(x, y, z);

		System.out.println("For the numbers " + c.getFirstInt() + ", " + c.getSecondInt() + " and " + c.getThirdInt());
		System.out.println("Largest is " + c.getLargest());
		System.out.println("Smallest is " + c.getSmallest());
		System.out.println("Sum is " + c.getSum());
		System.out.println("Product is " + c.getProduct());
		System.out.println("Average is " + c.getAverage());
	}
}
