public class DataRaceS extends Thread {

    static int common = 0;
    static Object lockObj;

    public DataRaceS(Object lockObj) {
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
        // Object lockObj = new Object();
        int max = 10000;
        DataRaceS[] allThreads = new DataRaceS[max];
        for (int i = 0; i < allThreads.length; i++) {
            allThreads[i] = new DataRaceS(new Object());
        }
        for (DataRaceS t : allThreads) {
            t.start();
        }
        for (DataRaceS t : allThreads) {
            t.join();
        }
        System.out.println(common); // will be 10000
    }
}
