import java.util.Scanner;

public class hello {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter your name: ");
		String yourName = in.nextLine();
		System.out.println("Hello " + yourName + "!");
		in.close();
	}
}
