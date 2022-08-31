/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

import javax.swing.JOptionPane;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class CakeApp {

    public static void main(String[] args) {
        Cake[] cakeList = new Cake[7];
        int quantity = 0;
        double totalPrice = 0.0;
        double highestPrice = 0.0;
        int index = 0;

        cakeList[0] = new OrderCake(4.5, "Butter", 50);
        cakeList[1] = new ReadyMadeCake(5, "Pound", 25);
        cakeList[2] = new ReadyMadeCake(3, "Sponge", 55);
        cakeList[3] = new OrderCake(14.5, "Genoise", 30);
        cakeList[4] = new OrderCake(11.5, "Biscuit", 38);
        cakeList[5] = new ReadyMadeCake(10, "Angel Food", 49);
        cakeList[6] = new ReadyMadeCake(2, "Chiffon", 15);

        for (quantity = 0; quantity < cakeList.length; quantity++) {
            double price = cakeList[quantity].calPrice();
            totalPrice += price;
            if (price > highestPrice) {
                highestPrice = price;
                index = quantity;
            }
        }
        System.out.println("Total price of all cakes sold " + totalPrice + "\n"
                + "ReadyMadeCake:\n"
                + "\tTotal quantity sold " + quantity + "\n"
                + "\tTotal price sold " + totalPrice + "\n"
                + "Highest Price Cake: " + cakeList[index].name
                + " " + cakeList[index].rate + " "
                + (int) (cakeList[index].calPrice() / cakeList[index].rate)
                + " pieces " + cakeList[index].calPrice());

        JOptionPane.showMessageDialog(null, "Total price of all cakes sold "
                + totalPrice + "\n"
                + "ReadyMadeCake:\n"
                + "  Total quantity sold " + quantity + "\n"
                + "  Total price sold " + totalPrice + "\n"
                + "Highest Price Cake: " + cakeList[index].name
                + " " + cakeList[index].rate + " "
                + (int) (cakeList[index].calPrice() / cakeList[index].rate)
                + " pieces " + cakeList[index].calPrice());
    }
}
