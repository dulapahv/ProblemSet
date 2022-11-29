class MySleep implements Runnable {
    public void run() {
        for (int i = 0; i < 50; i++) {
            System.out.println("run() : " + i);
            if (i == 10) {
                System.out.println("Nap Time");
                try {
                    Thread.currentThread().sleep(5000);// milli seconds
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

public class DoMySleep {
    public static void main(String[] args) {
        MySleep ms = new MySleep();
        Thread t = new Thread(ms);
        t.start();

        for (int i = 0; i < 50; i++) {
            System.out.println("main(): " + i);
        }
    }
}
