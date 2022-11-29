class MyQuitable2 implements Runnable {
    boolean go = true;

    public void quit() {
        go = false;
    }

    public void run() {
        for (int i = 0; go; i++) {
            System.out.println("run():  " + i);
        }
    }
}

public class DoAQuit2 {

    public static void main(String[] args) {
        MyQuitable2 mq = new MyQuitable2();
        Thread t = new Thread(mq);
        t.start();
        for (int i = 0; i < 2000; i++) {
            System.out.println("main(): " + i);
            if (i == 1000)
                mq.quit();
        }
    }
}
