package com.hackbulgaria.generics;

public class Box<T> {
    private T value;

    public Box() {
        this(null);
    }

    public Box(T value) {
        this.value = value;
    }

    public T getValue() {
        return this.value;
    }

    public void setValue(T value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return "Box [value=" + this.value + "]";
    }
}
