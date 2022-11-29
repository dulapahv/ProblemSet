class MyRunnable2 implements Runnable {
    MyRunnable2() {
        Thread t = new Thread(this);
        t.start();
    }

    public void run() {
        for (int i = 0; i < 2000; i++) {
            System.out.println("run():  " + i);
        }
    }
}

public class DoARunnable2 {
    public static void main(String[] args) {
        MyRunnable2 mr = new MyRunnable2();
        // or new MyRunnable2();
        for (int i = 0; i < 2000; i++) {
            System.out.println("main(): " + i);
        }
    }
}
