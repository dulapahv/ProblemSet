/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

import java.util.*;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class BookList {

    private ArrayList<Book> books;

    public BookList() {
        books = new ArrayList<>();
    }

    public void addBook(String t, String i, String a) {
        books.add(new Book(t, i, a));
    }

    public void displayBook() {
        for (Book book : books) {
            System.out.println(book);
        }
    }

    public static void main(String[] args) {
        BookList bList = new BookList();

        bList.addBook("Calculus", "1234", "Goldstein");
        bList.addBook("Java", "5678", "Gosling");
        bList.addBook("Algorithms", "4629", "Cormen");

        System.out.println("Show all books");
        bList.displayBook();

        System.out.println("\nSort by title");
        Collections.sort(bList.books, (Book o1, Book o2) -> o1.getTitle().compareTo(o2.getTitle()));
        bList.displayBook();

        System.out.println("\nSort by isbn");
        Collections.sort(bList.books, (Book o1, Book o2) -> o1.getIsbn().compareTo(o2.getIsbn()));
        bList.displayBook();

        System.out.println("\nSort by author");
        Collections.sort(bList.books, (Book o1, Book o2) -> o1.getAuthor().compareTo(o2.getAuthor()));
        bList.displayBook();
    }
}
