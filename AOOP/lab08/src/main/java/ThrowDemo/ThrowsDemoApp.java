/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ThrowDemo;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class ThrowsDemoApp {

    public static void main(String[] args) {
        try {
            ThrowsDemo.throwOne();
        } catch (IllegalAccessException e) {
            System.out.println("Catch " + e);

        }
    }
}
