package com.hackbulgaria.generics;

import java.util.Collection;
import java.util.List;

public class GenericUtilsDemo {
    public static void main(String[] args) {
        List<?> whatIsThis = GenericsUtils.asList(null, null, null);
        List<Object> hahaaah = GenericsUtils.asList(null, null, null);
        List<Integer> didNotExpectThisWTF = GenericsUtils.asList(null, null, null);
        System.out.println(whatIsThis);
        System.out.println(hahaaah);
        System.out.println(didNotExpectThisWTF);


        Collection<Integer> all = GenericsUtils.asList(1,2,3,4,5,6,7);
        Collection<Integer> filtered = GenericsUtils.greaterThan(all, 5); //6, 7
        System.out.println(filtered);

        Collection<String> trickyAll = GenericsUtils.asList("Potato", "Tomato", "Apple");
        Collection<String> trickyFiltered = GenericsUtils.greaterThan(trickyAll, "apple");
        System.out.println(trickyFiltered);
    }
 }
