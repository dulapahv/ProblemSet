/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Fish extends Pet implements Prey {

    public Fish(String name) {
        super(name);
    }

    @Override
    public void move() {
        super.move();
    }
    
    @Override
    public void isEaten(Predator p) {
        System.out.println(super.toString() + " is eaten by " + p.toString());
    }
}
