package com.hackbulgaria.corejava.exam1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ListUtils {
    public static List<Integer> sortList(List<Integer> list) {
        List<Integer> outputList = new ArrayList<Integer>();
        outputList.addAll(list);
        Collections.sort(outputList);
        return outputList;
    }

    public static List<Integer> reverseList(List<Integer> list) {
        List<Integer> outputList = new ArrayList<Integer>();
        outputList.addAll(list);
        Collections.reverse(outputList);
        return outputList;
    }

    public boolean isMonotonous(List<Integer> list) {
        return list.equals(sortList(new ArrayList<Integer>(list)))
                || list.equals(reverseList(sortList(new ArrayList<Integer>(list))));
    }
}
