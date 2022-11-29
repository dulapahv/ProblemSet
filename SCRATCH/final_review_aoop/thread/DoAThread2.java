class MyThread2 extends Thread {
    MyThread2() {
        start();
    }

    public void run() {
        for (int i = 0; i < 2000; i++) {
            System.out.println("run():  " + i);
        }
    }
}

public class DoAThread2 {
    public static void main(String[] args) {
        MyThread2 mt = new MyThread2();
        // or new MyThread2();

        for (int i = 0; i < 2000; i++) {
            System.out.println("main(): " + i);
        }
    }
}

// Data racing occur!
