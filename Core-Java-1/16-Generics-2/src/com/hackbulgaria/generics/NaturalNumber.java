package com.hackbulgaria.generics;

public class NaturalNumber<T extends Number> {
    private T value;

    public NaturalNumber(T value) {
        this.value = value;
    }

    public boolean isEven() {
        boolean output;
        try {
            output = Number.class.cast(this.value).intValue() % 2 == 0;
        } catch (ClassCastException e) {
            output = false;
        }
        return output;
    }
}
