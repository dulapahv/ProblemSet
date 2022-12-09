/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Cat extends Pet implements Playful, Talking, Predator {

    public Cat(String name) {
        super(name);
    }

    @Override
    public void move() {
        super.move();
    }

    @Override
    public void talk() {
        System.out.println(super.toString() + " talks");
    }

    @Override
    public void play() {
        System.out.println(super.toString() + " plays");
    }

    @Override
    public void eat(Prey p) {
        System.out.println(super.toString() + " eats " + p.toString());
    }
}
