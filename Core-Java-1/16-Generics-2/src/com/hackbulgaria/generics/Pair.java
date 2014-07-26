package com.hackbulgaria.generics;

public class Pair<F, S> {
    private F first;
    private S second;

    public Pair() {
        this(null, null);
    }

    public Pair(F first, S second) {
        this.first = first;
        this.second = second;
    }

    public F getFirst() {
        return this.first;
    }

    public void setFirst(F first) {
        this.first = first;
    }

    public S getSecond() {
        return this.second;
    }

    public void setSecond(S second) {
        this.second = second;
    }

    @Override
    public String toString() {
        return "Pair [first=" + this.first + ", second=" + this.second + "]";
    }

}
