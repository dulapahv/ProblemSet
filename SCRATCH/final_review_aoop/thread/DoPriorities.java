class MyPriority implements Runnable {
    String text;

    MyPriority(String s) {
        text = s;
    }

    public void run() {
        for (int i = 0; i < 500; i++) {
            System.out.println(text + i);
        }
    }
}

public class DoPriorities {
    public static void main(String[] args) {
        for (int j = 0; j < 10; j++) {
            MyPriority mr = new MyPriority("Runner " + j + ": ");
            Thread t = new Thread(mr);

            t.start();
        }
        for (int i = 0; i < 500; i++) {
            System.out.println("main(): " + i);
        }
    }
}
