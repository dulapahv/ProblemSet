/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class DiningHall {

    public static class MyThread implements Runnable {

        DiningHall d;

        public MyThread(DiningHall d) {
            this.d = d;
        }

        @Override
        public void run() {
            this.d.servePizza();
        }
    }

    static int pizzaNum;
    static int studentID;

    public void makePizza() {
        pizzaNum++;
    }

    synchronized public void servePizza() {
        String result;
        if (pizzaNum > 0) {
            result = "Served ";
            pizzaNum--;
        } else {
            result = "Starved ";
        }
        System.out.println(result + studentID);
        studentID++;
    }

    /*
    c. Describe what data races may occur in your multithreaded code without
       synchronization.

    If the DiningHall class is not thread-safe, then there may be data races
    when multiple threads access the same instance of the class. For example,
    two threads may try to increment the pizzaNum variable at the same time,
    resulting in an incorrect value. Alternatively, two threads may try to
    decrement the pizzaNum variable at the same time, resulting in a
    negative value.
     */
    public static void main(String[] args) {
        DiningHall d = new DiningHall();
        for (int i = 0; i < 10; i++) {
            d.makePizza();
        }
        for (int i = 0; i < 20; i++) {
            Thread thread = new Thread(new MyThread(d));
            thread.start();
        }

    }
}
