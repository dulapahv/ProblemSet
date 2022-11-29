class MyRunner implements Runnable {
    String text;

    MyRunner(String s) {
        text = s;
    }

    public void run() {
        for (int i = 0; i < 500; i++) {
            System.out.println(text + i);
        }
    }
}

public class DoRunnables {
    public static void main(String[] args) {
        for (int j = 0; j < 10; j++) {
            MyRunner mr = new MyRunner("Runner " + j + ": ");
            Thread t = new Thread(mr);
            t.start();
        }
        for (int i = 0; i < 500; i++) {
            System.out.println("main(): " + i);
        }
    }
}
