/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class TesterException {

    public static void main(String args[]) {
        Slip firstSlip = null;
        try {
            firstSlip = new Slip(150, 10, 25);
            System.out.println(firstSlip);
        } catch (Exception n) // display exception message
        {
            System.out.println(n);
        }

        try {
            firstSlip = new Slip(1, 15, 25);
            System.out.println(firstSlip);
        } catch (Exception n) // display exception message
        {
            System.out.println(n);
        } finally {
            System.out.println("finally block is always executed");
        }

        try {
            firstSlip = new Slip(2, 10, 25);
            System.out.println(firstSlip);
        } catch (Exception n) {
            System.out.println(n);
        } finally {
            System.out.println("finally block is always executed");
        }
    }
}
