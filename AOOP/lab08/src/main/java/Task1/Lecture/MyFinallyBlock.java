/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1.Lecture;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class MyFinallyBlock {

    public static void main(String[] args) {
        /**
         * Exception will occur here, after catch block the contol will goto
         * finally block.
         */
        try {
            int i = 10 / 0;
        } catch (Exception ex) {
            System.out.println("Inside 1st catch Block");
        } finally {
            System.out.println("Inside 1st finally block");
        }
        /**
         * In this case exception won't, after executing try block the contol
         * will goto finally block.
         */
        try {
            int i = 10 / 10;
        } catch (Exception ex) {
            System.out.println("Inside 2nd catch Block");
        } finally {
            System.out.println("Inside 2nd finally block");
        }

    }
}
