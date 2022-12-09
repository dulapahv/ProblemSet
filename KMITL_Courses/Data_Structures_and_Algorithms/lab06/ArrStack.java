public class ArrStack {
	static int max = 1000;
	int top = 0;
	double[] stack = new double[max];

	public void push(double x) {
		stack[top] = x;
		top++;
	}

	public double pop() {
		top--;
		return stack[top];
	}

	public double top() {
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