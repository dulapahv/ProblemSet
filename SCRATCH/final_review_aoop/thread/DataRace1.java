public class DataRace1 extends Thread {

    static int common = 0;
    Object lockObj; // Not static

    public DataRace1(Object lockObj) {
        this.lockObj = lockObj;
    }

    public void run() {
        synchronized (lockObj) {// only one thread will be allowed
            int local = common; // data race eliminated
            local = local + 1;
            common = local;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Object lockObj = new Object();
        int max = 10000;
        DataRace1[] allThreads = new DataRace1[max];
        for (int i = 0; i < allThreads.length; i++) {
            allThreads[i] = new DataRace1(lockObj);
        }
        for (DataRace1 t : allThreads) {
            t.start();
        }
        for (DataRace1 t : allThreads) {
            t.join();
        }
        System.out.println(common); // will be 10000
    }
}
