/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task2;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Book {

    private String title;
    private String isbn;
    private String author;

    public Book(String title, String isbn, String author) {
        this.title = title;
        this.isbn = isbn;
        this.author = author;
    }

    public String getTitle() {
        return this.title;
    }

    public String isbn() {
        return this.isbn;
    }

    public String author() {
        return this.author;
    }

    @Override
    public String toString() {
        return "title: " + title + ", isbn: " + isbn + ", author: " + author;
    }
}
