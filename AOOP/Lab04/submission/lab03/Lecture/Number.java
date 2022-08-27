public class Number {
	int num;

	public Number(int num) {
		this.num = num;
	}

	public int getNumber() {
		return num;
	}

	public Number add(Number op) {
		int num1, num2;
		num1 = this.getNumber();
		num2 = op.getNumber();
		Number sum = new Number(num1 + num2);
		return sum;
	}

	@Override
	public String toString() {
		return this.getNumber() + " ";
	}
}
