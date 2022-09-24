/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1.creatingexception;

/**
 *
 * @author Dulapah Vibulsanti
 */
import java.util.Scanner;

public class CreatingException {

    // This method must declare that it throws a OutOfRangeException .
    public static void main(String[] args) throws OutOfRangeException {
        final int MIN = 25, MAX = 40;
        Scanner scan = new Scanner(System.in);
        //OutOfRangException problem = new OutOfRangException("Input value is out of range.");
        System.out.print("Enter an integer value between " + MIN + " and " + MAX + ", inclusive: ");
        int value = scan.nextInt();
        //Determine if the exception should be thrown
        if (value < MIN || value > MAX) {
            throw new OutOfRangeException("Input value is out of range");
        }
        System.out.println("End of main method.");
    }

}
