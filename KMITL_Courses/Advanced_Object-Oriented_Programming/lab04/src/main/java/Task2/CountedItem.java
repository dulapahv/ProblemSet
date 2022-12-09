/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class CountedItem extends PurchaseItem {
	private int quantity;

	public CountedItem() {
		super();
		this.quantity = 0;
	}

	public int getQuantity() {
		return this.quantity;
	}

	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}

	@Override
	public double getPrice() {
		return super.getPrice() * this.quantity;
	}

	@Override
	public String toString() {
		return (this.getName() + " @ " + super.getPrice() + " " + quantity + " units " + this.getPrice() + " $");
	}
}
