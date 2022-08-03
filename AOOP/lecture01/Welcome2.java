public class Welcome2 {
	public static void main(String[] args) {
		System.out.println(Fi.getK());

		Fe f = new Fe();
		System.out.println(f.getI());
		System.out.println(f.getISquare());
	}
}

class Fe {
	int i = 4;

	int getI() {
		return i;
	}

	double getISquare() {
		return Math.pow(i, 2);
	}
}

class Fi {
	static int k = 2;

	static int getK() {
		return k;
	}
}