package com.hackbulgaria.generics;

public class FavouritesDemo {
    public static void main(String[] args) {
        Favourites favourites = new Favourites();
        favourites.add(String.class, "Kartof");
        favourites.add(Integer.class, 5);
        System.out.println(favourites.get(String.class));
    }
}
