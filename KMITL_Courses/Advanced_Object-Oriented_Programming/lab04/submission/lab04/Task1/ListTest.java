/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class ListTest {

	public static void main(String[] args) {
		IntList myList = new IntList(10);
		myList.add(100);
		myList.add(50);
		myList.add(200);
		myList.add(25);
		System.out.println("My List:\n" + myList);
		SortedIntList mySortedList = new SortedIntList(10);
		mySortedList.add(100);
		mySortedList.add(50);
		mySortedList.add(200);
		mySortedList.add(25);
		System.out.println("My Sorted List:\n" + mySortedList);
	}
}
