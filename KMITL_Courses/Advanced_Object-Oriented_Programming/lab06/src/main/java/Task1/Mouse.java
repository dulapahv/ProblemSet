/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Mouse extends Animal implements Talking, Prey {

    @Override
    public String toString() {
        return "The Mouse";
    }

    @Override
    public void move() {
        super.move();
    }

    @Override
    public void talk() {
        System.out.println(this.toString() + " talks");
    }

    @Override
    public void isEaten(Predator p) {
        System.out.print(this.toString() + " is eaten by " + p.toString());
    }
}
