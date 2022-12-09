import java.util.Scanner;

public class CalculationApp {
	public static void main(String[] args) {
		int x = 0, y = 0, z = 0;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter first integer: ");
		x = scan.nextInt();
		System.out.print("Enter second integer: ");
		y = scan.nextInt();
		System.out.print("Enter third integer: ");
		z = scan.nextInt();
		scan.close();

		int max = Math.max(x, Math.max(y, z));
		int min = Math.min(x, Math.min(y, z));
		int sum = x + y + z;
		int prod = x * y * z;
		int avg = sum / 3;

		System.out.println("For the numbers " + x + ", " + y + " and " + z);
		System.out.println("Largest is " + max);
		System.out.println("Smallest is " + min);
		System.out.println("Sum is " + sum);
		System.out.println("Product is " + prod);
		System.out.println("Average is " + avg);
	}
}
