/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class PurchaseItem {
	private String name;
	private double unitPrice;

	public PurchaseItem() {
		this.name = "no item";
		this.unitPrice = 0;
	}

	public double getPrice() {
		return this.unitPrice;
	}

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setPrice(double price) {
		this.unitPrice = price;
	}

	@Override
	public String toString() {
		return (name + " @ " + unitPrice);
	}
}
