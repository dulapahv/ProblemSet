/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class CD implements Media {

    private Integer id;
    private String artist;
    private String title;
    private int year;

    public CD(Integer id, String artist, String title, int year) {
        this.id = id;
        this.artist = artist;
        this.title = title;
        this.year = year;
    }

    @Override
    public <T> Comparable<T> getId() {
        return (Comparable<T>) id;
    }

    @Override
    public <T> Comparable<T> getCreator() {
        return (Comparable<T>) artist;
    }

    @Override
    public String getTitle() {
        return this.title;
    }

    @Override
    public int getYear() {
        return this.year;
    }

}
