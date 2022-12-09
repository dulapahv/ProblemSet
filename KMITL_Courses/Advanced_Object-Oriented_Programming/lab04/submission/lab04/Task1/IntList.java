/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class IntList {
	protected int[] list;
	protected int numElements = 0;

	public IntList(int size) {
		list = new int[size];
	}

	public void add(int value) {
		if (numElements == list.length) {
			System.out.println("Can't add, list is full");
		} else {
			list[numElements] = value;
			numElements++;
		}
	}

	@Override
	public String toString() {
		String returnString = "";
		for (int i = 0; i < numElements; i++) {
			returnString += i + ": " + list[i] + "\n";
		}
		return returnString;
	}
}
