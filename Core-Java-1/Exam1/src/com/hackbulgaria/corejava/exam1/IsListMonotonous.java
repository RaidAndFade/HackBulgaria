package com.hackbulgaria.corejava.exam1;

import java.util.ArrayList;
import java.util.List;

public class IsListMonotonous {
    public boolean isMonotonous(List<Integer> list) {
        return list.equals(ListSort.sortList(new ArrayList<Integer>(list))) || list.equals(ListReverse.reverseList(ListSort.sortList(new ArrayList<Integer>(list))));
    }
}
