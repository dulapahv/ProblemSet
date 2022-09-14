/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class Book implements Media {

    private String id;
    private String author;
    private String title;
    private int yearPublished;

    public Book(String id, String author, String title, int yearPublished) {
        this.id = id;
        this.author = author;
        this.title = title;
        this.yearPublished = yearPublished;
    }

    @Override
    public <T> Comparable<T> getId() {
        return (Comparable<T>) id;
    }

    @Override
    public <T> Comparable<T> getCreator() {
        return (Comparable<T>) author;
    }

    @Override
    public String getTitle() {
        return this.title;
    }

    @Override
    public int getYear() {
        return this.yearPublished;
    }

}
