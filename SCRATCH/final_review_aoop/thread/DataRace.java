public class DataRace extends Thread {

    static int common = 0;

    public void run() {
        int local = common; // data race
        local = local + 1;
        common = local; // data race
    }

    public static void main(String[] args) throws InterruptedException {
        int max = 10000;
        DataRace[] allThreads = new DataRace[max];
        for (int i = 0; i < allThreads.length; i++) {
            allThreads[i] = new DataRace();
        }
        for (DataRace t : allThreads) {
            t.start();
        }
        for (DataRace t : allThreads) {
            t.join();
        }
        System.out.println(common); // may not be 10000
    }
}
