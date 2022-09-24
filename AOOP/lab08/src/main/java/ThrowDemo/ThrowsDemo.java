/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ThrowDemo;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class ThrowsDemo {

    static void throwOne() throws IllegalAccessException {
        System.out.println("Inside ThrowsOne()");
        throw new IllegalAccessException("Demo");
    }
}
