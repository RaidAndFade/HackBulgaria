package com.hackbulgaria.generics;

public class PairDemo {
    public static void main(String[] args) {
        Pair<Integer, Integer> pair = new Pair<>();
        pair.setFirst(3);
        int first = pair.getFirst();
        System.out.println(first);
    }
}
