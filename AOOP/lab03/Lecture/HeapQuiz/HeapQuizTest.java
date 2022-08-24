public class HeapQuizTest {
	public static void main(String[] args) {
		// TODO code application logic here
		int x = 0;
		HeapQuiz[] hq = new HeapQuiz[5];
		while (x < 3) {
			hq[x] = new HeapQuiz();
			hq[x].id = x;
			x = x + 1;
		}

		for (int j = 0; j < hq.length; j++) {
			System.out.println(hq[j]);
		}
	}
}
