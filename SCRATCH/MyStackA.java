public class MyStackA {
	int MAX_SIZE = 100;
	double stack[] = new double[MAX_SIZE];
	int top = 0;

	public void push(double d) {
		stack[top++] = d;
	}

	public double pop() {
		return stack[--top];
	}

	public double top() {
		return stack[top - 1];
	}

	public boolean isFull() {
		return top == MAX_SIZE;
	}

	public boolean isEmpty() {
		return top == 0;
	}
}