/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Task2 {

	public static void main(String[] args) {
		WeightedItem w1 = new WeightedItem();
		w1.setName("Banana");
		w1.setPrice(3.00);
		w1.setWeight(1.37);
		System.out.println(w1);

		CountedItem c1 = new CountedItem();
		c1.setName("Pen");
		c1.setPrice(4.5);
		c1.setQuantity(10);
		System.out.println(c1);
	}
}
