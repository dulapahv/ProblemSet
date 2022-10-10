public class factorial {
	public static int fact(int n) {
		if (n == 0)
			return 1;
		return n * fact(n - 1);
	}

	public static int factLoop(int n) {
		int r = 1;
		while (n > 0) {
			r *= n;
			n--;
		}
		return r;
	}

	public static void main(String[] args) {
		System.out.println(fact(5));
		System.out.println(factLoop(5));
	}
}