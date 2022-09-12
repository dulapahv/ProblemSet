public class ArrStackString {
	static int max = 1000;
	int top = 0;
	String[] stack = new String[max];

	public void push(String x) {
		stack[top] = x;
		top++;
	}

	public String pop() {
		top--;
		return stack[top];
	}

	public String top() {
		return stack[top - 1];
	}

	public boolean isEmpty() {
		return top == 0;
	}

	public boolean isFull() {
		return top == max;
	}

	@Override
	public String toString() {
		String s = "";
		for (int i = 0; i < top; i++) {
			s += stack[i] + " ";
		}
		return s;
	}
}