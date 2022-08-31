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
        double totalReadyMadeCakePrice = 0.0;
        double highestPrice = 0.0;
        String highestMsg = "";

        cakeList[0] = new OrderCake(4.5, "Butter", 50);
        cakeList[1] = new ReadyMadeCake(5, "Pound", 25);
        cakeList[2] = new ReadyMadeCake(3, "Sponge", 55);
        cakeList[3] = new OrderCake(14.5, "Genoise", 30);
        cakeList[4] = new OrderCake(11.5, "Biscuit", 38);
        cakeList[5] = new ReadyMadeCake(10, "Angel Food", 49);
        cakeList[6] = new ReadyMadeCake(2, "Chiffon", 15);

        for (int i = 0; i < cakeList.length; i++) {
            double price = cakeList[i].calPrice();
            totalPrice += price;
            if (cakeList[i] instanceof ReadyMadeCake) {
                quantity += ((ReadyMadeCake) cakeList[i]).getQuantity();
                totalReadyMadeCakePrice += cakeList[i].calPrice();
            }
            if (price > highestPrice) {
                highestPrice = price;
                if (cakeList[i] instanceof ReadyMadeCake) {
                    highestMsg = ((ReadyMadeCake) cakeList[i]).getName()
                            + " " + ((ReadyMadeCake) cakeList[i]).getRate()
                            + " " + ((ReadyMadeCake) cakeList[i]).getQuantity()
                            + " pieces " + ((ReadyMadeCake) cakeList[i]).calPrice();
                } else {
                    highestMsg = ((OrderCake) cakeList[i]).getName()
                            + " " + ((OrderCake) cakeList[i]).getRate()
                            + " " + ((OrderCake) cakeList[i]).getWeight()
                            + " pounds " + ((OrderCake) cakeList[i]).calPrice();
                }
            }
        }

        System.out.println("Total price of all cakes sold: " + totalPrice + "\n"
                + "ReadyMadeCake:\n"
                + "\tTotal quantity sold " + quantity + "\n"
                + "\tTotal price sold " + totalReadyMadeCakePrice + "\n"
                + "Highest Price Cake: " + highestMsg);

        JOptionPane.showMessageDialog(null, "Total price of all cakes sold: " + totalPrice + "\n"
                + "ReadyMadeCake:\n"
                + "  Total quantity sold " + quantity + "\n"
                + "  Total price sold " + totalReadyMadeCakePrice + "\n"
                + "Highest Price Cake: " + highestMsg);
    }
}
