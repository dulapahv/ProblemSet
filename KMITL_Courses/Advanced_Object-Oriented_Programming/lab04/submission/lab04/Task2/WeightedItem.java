/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class WeightedItem extends PurchaseItem {
	private double weight;

	public WeightedItem() {
		super();
		this.weight = 0;
	}

	public double getWeight() {
		return this.weight;
	}

	public void setWeight(double weight) {
		this.weight = weight;
	}

	@Override
	public double getPrice() {
		return super.getPrice() * this.weight;
	}

	@Override
	public String toString() {
		return (this.getName() + " @ " + super.getPrice() + " " + weight + "Kg " + this.getPrice() + " $");
	}
}
