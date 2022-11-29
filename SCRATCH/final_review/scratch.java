// demonstrate synchronize and lock

public class scratch {
    public static void main(String[] args) {
        counter c = new counter();
        Thread t1 = new Thread(c);
        Thread t2 = new Thread(c);
        t1.start();
        t2.start();
    }
}

class counter implements Runnable {
    private int count = 0;
    private Object lock = new Object();

    public void run() {
        synchronized (lock) {
            count++;
            System.out.println("Count is: " + count);
        }
    }
}

// Output:
// Count is: 1
// Count is: 2