package com.hackbulgaria.corejava.exam1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ListReverse {
    public static List<Integer> reverseList(List<Integer> list) {
        List<Integer> outputList = new ArrayList<Integer>();
        Collections.reverse(list);
        outputList.addAll(list);
        return outputList;
    }
}
