/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
import java.util.InputMismatchException;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;

public class main {

    public static void main(String[] args) {
        int total = 0;
        int num = 0;

        File myFile = null;
        Scanner inputFile = null;

        myFile = new File("src/main/java/Task1/inFile.txt");
        try {
            inputFile = new Scanner(myFile);
        } catch (FileNotFoundException ex) {
            System.out.println(ex);
        }

        while (inputFile.hasNext()) {
            try {
                num = inputFile.nextInt();
                total += num;
            } catch (InputMismatchException ex) {
                System.out.println("Illegal value found");
                inputFile.next();
            }
        }

        System.out.println("The total value is " + total);
    }
}
