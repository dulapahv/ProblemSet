public class Calculation {
	private int x, y, z;

	Calculation(int dX, int dY, int dZ) {
		x = dX;
		y = dY;
		z = dZ;
	}

	int getFirstInt() {
		return x;
	}

	int getSecondInt() {
		return y;
	}

	int getThirdInt() {
		return z;
	}

	int getLargest() {
		return Math.max(x, Math.max(y, z));
	}

	int getSmallest() {
		return Math.min(x, Math.min(y, z));
	}

	int getSum() {
		return x + y + z;
	}

	int getProduct() {
		return x * y * z;
	}

	int getAverage() {
		return getSum() / 3;
	}
}
