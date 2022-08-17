import java.util.Scanner;
import java.util.Arrays;

public class Lotto {
	public static void main(String[] args) {
		// TODO code application logic here
		int[] winninglotto = { 12, 35, 34, 2, 5 };
		int[] userlotto = new int[5];
		int numberMatch = 0;

		Scanner input = new Scanner(System.in);

		for (int i = 0; i < userlotto.length; i++) {
			System.out.println("Enter your lotto number " + (i + 1) + ":");
			userlotto[i] = input.nextInt();
		}

		Arrays.sort(winninglotto);

		for (int num : userlotto) {
			// binarySearch returns -1 if not matched,
			numberMatch += (Arrays.binarySearch(winninglotto, num) < 0) ? 0 : 1; // conditional if, += 0 if the
																					// statement is false, += 1 if true
		}

		System.out.println(numberMatch);
		System.out.println((numberMatch == 0) ? "o matching numbers: $0"
				: (numberMatch == 1) ? "1 matching numbers: $1"
						: (numberMatch == 2) ? "2 matching numbers: $50"
								: (numberMatch == 3) ? "3 matching numbers: 10,000$"
										: (numberMatch == 4) ? "4 matching numbers: $50,000"
												: "5 matching numbers: $90,000,000");

	}

}
