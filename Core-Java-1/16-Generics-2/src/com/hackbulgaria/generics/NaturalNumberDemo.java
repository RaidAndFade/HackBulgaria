package com.hackbulgaria.generics;

public class NaturalNumberDemo {
    public static void main(String[] args) {
        NaturalNumber<Long> n1 = new NaturalNumber<>(12341541L);
        NaturalNumber<Integer> n2 = new NaturalNumber<>(123);
        NaturalNumber<Short> n3 = new NaturalNumber<>((short) 122);

        System.out.println(n1.isEven()); // false;
        System.out.println(n2.isEven()); // false;
        System.out.println(n3.isEven()); // true;

        // as expected, it shouldn't be allowed
        // NaturalNumber<String> n4 = new NaturalNumber<Strinfg>("4");
    }
}
