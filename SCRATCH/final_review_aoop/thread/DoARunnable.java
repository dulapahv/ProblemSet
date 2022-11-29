class MyRunnable implements Runnable {
    public void run() {
        for (int i = 0; i < 2000; i++) {
            System.out.println("run():  " + i);
        }
    }
}

public class DoARunnable {
    public static void main(String[] args) {
        MyRunnable mr = new MyRunnable();
        Thread t = new Thread(mr);
        t.start();
        for (int i = 0; i < 2000; i++) {
            System.out.println("main(): " + i);
        }
    }
}
