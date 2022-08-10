import java.util.Scanner;

public class PasswordApp {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (true) {
			System.out.print("Enter a password: ");
			String passwd = in.nextLine();

			if (PasswordVerifier.isValid(passwd)) {
				System.out.println("Valid password.");
				break;
			} else {
				System.out.println("Invalid password.");
			}
		}
		in.close();
	}
}
