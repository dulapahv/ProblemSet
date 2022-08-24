/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class SortedIntList extends IntList {
	public SortedIntList(int size) {
		super(size);
	}

	public void add(int value) {
		if (numElements == list.length) {
			System.out.println("Can't add, list is full");
		} else {
			int i = 0;
			while (i < numElements && list[i] < value) {
				i++;
			}
			for (int j = numElements; j > i; j--) {
				list[j] = list[j - 1];
			}
			list[i] = value;
			numElements++;
		}
	}
}