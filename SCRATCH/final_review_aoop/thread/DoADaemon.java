class MyDaemon implements Runnable {
    public void run() {
        for (int i = 0; true; i++) {
            System.out.println("run():  " + i);
        }
    }
}

public class DoADaemon {
    public static void main(String[] args) {
        MyDaemon md = new MyDaemon();
        Thread t = new Thread(md);
        t.setDaemon(true);
        t.start();
        for (int i = 0; i < 2000; i++) {
            System.out.println("main(): " + i);

        }
    }
}
