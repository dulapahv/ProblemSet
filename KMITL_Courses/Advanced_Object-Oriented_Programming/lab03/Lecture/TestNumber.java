public class TestNumber {

	public static void main(String[] args) {
		Number num1, num2;
		Number result;
		num1 = new Number(10);
		num2 = new Number(5);

		result = num1.add(num2);
		System.out.println(result);
	}
}