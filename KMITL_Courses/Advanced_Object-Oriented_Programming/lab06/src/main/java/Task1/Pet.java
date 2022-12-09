/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public abstract class Pet extends Animal {

    private String name;

    protected Pet(String name) {
        this.name = name;
    }
    
    @Override
    public String toString() {
        return this.name;
    }
}
