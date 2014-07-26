package com.hackbulgaria.generics;

import java.util.LinkedList;
import java.util.List;

public class Favourites {
    List<Object> list;

    public Favourites() {
        this.list = new LinkedList<Object>();
    }

    public <T> void add(Class<T> aClass, T element) {
        T toAdd = aClass.cast(element);
        this.list.add(toAdd);
    }

    public <T> List<T> get(Class<T> aClass) {
        List<T> outputList = new LinkedList<T>();
        for (Object element : this.list) {
            if (element.getClass().equals(aClass)) {
                outputList.add(aClass.cast(element));
            }
        }
        return outputList;
    }
}
