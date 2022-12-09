/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class App {

    public static void main(String[] args) {
        Animal[] animals = new Animal[4];
        animals[0] = new Dog("Fido");
        animals[1] = new Fish("Max");
        animals[2] = new Mouse();
        animals[3] = new Cat("Fluffy");
        System.out.println();
        for (Animal a : animals) {
            System.out.println("==========");
            a.move();
            if (a instanceof Playful) {
                ((Playful) a).play();
            }
            if (a instanceof Talking) {
                ((Talking) a).talk();
            }
            if (a instanceof Predator) {
                for (Animal a2 : animals) {
                    if (a2 instanceof Prey) {
                        ((Predator) a).eat((Prey) a2);
                        ((Prey) a2).isEaten((Predator) a);
                    }
                }// inner loop on all animals
            }
        }// outer loop on all animals
    }// test method
}
