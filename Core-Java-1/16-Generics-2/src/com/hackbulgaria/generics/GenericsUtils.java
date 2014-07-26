package com.hackbulgaria.generics;

import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

public class GenericsUtils {
    public static <T> T newInstance(Class<T> aClass) throws InstantiationException, IllegalAccessException {
        return aClass.newInstance();
    }

    @SafeVarargs
    public static <T> List<T> asList(T... elements) {
        List<T> outputList = new LinkedList<T>();
        for (T t : elements) {
            outputList.add(t);
        }
        return outputList;
    }

    public static <T extends Comparable<T>> List<T> greaterThan(Collection<T> collection, T predicate) {
        List<T> outputList = new LinkedList<T>();
        for (T element : collection) {
            if (element.compareTo(predicate) > 0) {
                outputList.add(element);
            }
        }
        return outputList;
    }
}
