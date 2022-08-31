/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class OrderCake extends Cake {

    private double weight;

    public OrderCake(double weight, String name, double rate) {
        super(name, rate);
        this.weight = weight;
    }

    @Override
    public double calPrice() {
        return this.rate * this.weight;
    }
}
