import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.regex.Pattern;

public class ComputeInfix {

	private static boolean isNumeric(String str) {
		Pattern pattern = Pattern.compile("-?\\d+(\\.\\d+)?");
		return pattern.matcher(str).matches();
	}

	public static void main(String[] args) {
		ArrStackString stack = new ArrStackString();
		Scanner sc = new Scanner(System.in);
		MyQueueA queue = new MyQueueA();
		System.out.println("Enter an infix expression: ");
		String input = sc.nextLine();
		StringTokenizer st = new StringTokenizer(input);

		while (st.hasMoreTokens()) {
			String token = st.nextToken();
			if (token.matches("[0-9]+")) {
				queue.enqueue(token);
			} else if (token.matches("[()+/*-]")) {
				if (stack.isEmpty()) {
					stack.push(token);
				} else if (token.equals("(")) {
					stack.push(token);
				} else if (token.equals(")")) {
					while (!stack.top().equals("(")) {
						queue.enqueue(stack.pop());
					}
					stack.pop();
				} else if (token.equals("+") || token.equals("-")) {
					while (!stack.isEmpty() && !stack.top().equals("(")) {
						queue.enqueue(stack.pop());
					}
					stack.push(token);
				} else if (token.equals("*") || token.equals("/")) {
					while (!stack.isEmpty() && (stack.top().equals("*") || stack.top().equals("/"))) {
						queue.enqueue(stack.pop());
					}
					stack.push(token);
				}
			}
		}
		while (!stack.isEmpty()) {
			queue.enqueue(stack.pop());
		}

		ArrStack stack2 = new ArrStack();
		StringTokenizer st2 = new StringTokenizer(queue.toString());
		while (st2.hasMoreTokens()) {
			String token2 = st2.nextToken();
			if (isNumeric(token2)) {
				stack2.push(Double.parseDouble(token2));
			} else {
				switch (token2) {
					case "+" -> {
						double b = stack2.pop();
						double a = stack2.pop();
						stack2.push(a + b);
					}
					case "-" -> {
						double b = stack2.pop();
						double a = stack2.pop();
						stack2.push(a - b);
					}
					case "*" -> {
						double b = stack2.pop();
						double a = stack2.pop();
						stack2.push(a * b);
					}
					case "/" -> {
						double b = stack2.pop();
						double a = stack2.pop();
						stack2.push(a / b);
					}
				}
			}
		}
		System.out.println("Result: " + stack2.pop());
		sc.close();
	}
}
