/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Client {

    public static void main(String args[]) {

        Person[] person = new Person[3];
        person[0] = new Student();
        person[1] = new NewsAnchor();
        person[2] = new NewspaperEditor();

        System.out.println("\nEveryone is hard at work:");
        for (Person p : person) {
            System.out.print(p + " ");
            p.read();
        }

        System.out.println("\nEveryone goes back home after a long day:");
        for (Person p : person) {
            if (!(p instanceof Student)) {
                p.setReadingBehavior(new FunReading());
            }
            System.out.print(p + " ");
            p.read();
        }
    }// main class
}// Client class
