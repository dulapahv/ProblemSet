/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package Task1;

import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class CatalogApp {

    public static void main(String[] args) {
        //Create an ArrayList of CatalogItems named list1
        //This ArrayList must take a type parameter of CatalogItem
        //CatalogItem in turn should take a type parameter CD
        List<CatalogItem<CD>> list1 = new ArrayList<>();

        //adding CatalogItems	
        list1.add(new CatalogItem<CD>(new CD(0, "Lady Gaga", "The Fame", 2008)));
        list1.add(new CatalogItem<CD>(new CD(7, "Lady Gaga", "The Fame Monster", 2009)));
        list1.add(new CatalogItem<CD>(new CD(5, "Jay-Z", "The Blueprint 3", 2009)));
        list1.add(new CatalogItem<CD>(new CD(2, "Santana", "Supernatural", 1999)));

        //printing the iPod catalog before and after sorting
        System.out.println("CD Catalog:");
        System.out.println("Before Sorting:");
        //show list1 using Iterator;
        Iterator it1 = list1.iterator();
        while (it1.hasNext()) {
            System.out.println(it1.next());
        }
        //sort list1 by ID;
        Collections.sort(list1);
        System.out.println("\nAfter Sorting by ID:");
        //show list1 using Iterator;
        it1 = list1.iterator();
        while (it1.hasNext()) {
            System.out.println(it1.next());
        }
        //sort list1 by Artist;
        Collections.sort(list1, new CatalogItem.CreatorComparator<CD>());
        System.out.println("\nAfter Sorting by Artist:");
        //show list1 using Iterator;
        it1 = list1.iterator();
        while (it1.hasNext()) {
            System.out.println(it1.next());
        }

        //Create an ArrayList of CatalogItems named list2
        //This ArrayList must take a type parameter of CatalogItem
        //CatalogItem in turn should take a type parameter Book
        List<CatalogItem<Book>> list2 = new ArrayList<>();

        //adding CatalogItems
        list2.add(new CatalogItem<Book>(new Book("B5", " Atlas Shrugged ", " Ayn Rand ", 1957)));
        list2.add(new CatalogItem<Book>(new Book("A0", " Lord of the Rings: Fellowship of the Ring ", " J.R.R. Tolkien ", 1954)));
        list2.add(new CatalogItem<Book>(new Book("C2", " Even Cowgirls Get the Blues ", " Tom Robbins ", 1976)));
        list2.add(new CatalogItem<Book>(new Book("A1", " The Subtle Knife ", " Philip Pullman ", 1997)));

        //printing the kindle catalog before and after sorting
        System.out.println("\n\nBook Catalog:");
        System.out.println("Before Sorting:");
        //show list2 using Iterator;
        Iterator it2 = list2.iterator();
        while (it2.hasNext()) {
            System.out.println(it2.next());
        }
        //sort list2 by ID;
        Collections.sort(list2);
        System.out.println("\nAfter Sorting by ID:");
        //show list2 using Iterator;
        it2 = list2.iterator();
        while (it2.hasNext()) {
            System.out.println(it2.next());
        }
        //sort list2 by Creator;
        Collections.sort(list2, new CatalogItem.CreatorComparator<Book>());
        System.out.println("\nAfter Sorting by Author:");
        //show list2 using Iterator;
        it2 = list2.iterator();
        while (it2.hasNext()) {
            System.out.println(it2.next());
        }
    }
}
