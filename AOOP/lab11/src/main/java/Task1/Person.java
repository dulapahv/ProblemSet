/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Person {

    protected ReadingBehavior readingBehavior;

    public void setReadingBehavior(ReadingBehavior rb) {
        readingBehavior = rb;
    }

    public void read() {
        readingBehavior.read();
    }

    @Override
    public String toString() {
        return "The " + getClass().getSimpleName();
    }
}
