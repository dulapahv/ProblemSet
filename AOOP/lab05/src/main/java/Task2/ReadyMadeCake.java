/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class ReadyMadeCake extends Cake {

    private int quantity;

    public ReadyMadeCake(int quantity, String name, double rate) {
        super(name, rate);
        this.quantity = quantity;
    }

    @Override
    public double calPrice() {
        return this.rate * this.quantity;
    }
}
