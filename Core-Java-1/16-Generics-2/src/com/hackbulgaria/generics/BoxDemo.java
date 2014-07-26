package com.hackbulgaria.generics;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class BoxDemo {
    public static void main(String[] args) {
        Box<Integer> example = new Box<Integer>();
        example.setValue(5);
        System.out.println(example.getValue());
        Box<List<Integer>> exampleList = new Box<List<Integer>>(new LinkedList(Arrays.asList(5, 4, 3, 2)));
        System.out.println(exampleList.getValue());
        System.out.println(exampleList);
    }
}