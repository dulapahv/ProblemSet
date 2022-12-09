public class Payment {
	private static double salary;

	static String getPayment(double basePay, int hour) {
		String payStr = "";
		if (basePay < 8.0)
			payStr = "Base pay must be >= 8.00";
		if (hour > 60)
			payStr = "Hour worked must be <= 60";
		if (basePay >= 8.0 && hour <= 60) {
			if (hour <= 40)
				salary = hour * basePay;
			else {
				salary = 40 * basePay;
				salary += (hour - 40) * (basePay * 1.5);
			}
			payStr = "Pay $" + salary;
		}
		return payStr;
	}
}
