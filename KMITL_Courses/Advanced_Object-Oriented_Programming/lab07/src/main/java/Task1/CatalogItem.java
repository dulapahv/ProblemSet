/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Task1;

/**
 *
 * @author Dulapah Vibulsanti
 */
public class CatalogItem<S extends Media> implements Comparable<CatalogItem<S>> {

    private S media;

    public CatalogItem(S media) {
        this.media = media;
    }

    @Override
    public int compareTo(CatalogItem<S> o) {
        return media.getId().compareTo(o.media.getId());
    }

    public static class CreatorComparator<S extends Media> implements java.util.Comparator<CatalogItem<S>> {

        @Override
        public int compare(CatalogItem<S> o1, CatalogItem<S> o2) {
            return o1.media.getCreator().compareTo(o2.media.getCreator());
        }

    }

    @Override
    public String toString() {
        return media.getId() + ": " + media.getCreator() + ": " + media.getTitle() + ": " + media.getYear();
    }
}
