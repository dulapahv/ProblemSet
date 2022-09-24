/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Lecture;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Zero {

    public static void main(String[] args) {
        int numberator = 10;
        int deniminator = 0;
        try {
            System.out.println(numberator / deniminator);
        } catch (ArithmeticException e) {
            System.out.println(e);
            System.out.println("This text not be printed");
        }
    }
}
