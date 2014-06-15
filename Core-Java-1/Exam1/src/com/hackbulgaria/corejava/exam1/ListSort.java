package com.hackbulgaria.corejava.exam1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ListSort {
   public static List<Integer> sortList(List<Integer> list) {
       List<Integer> outputList = new ArrayList<Integer>();
       Collections.sort(list);
       outputList.addAll(list);
       return outputList;
   }
}
