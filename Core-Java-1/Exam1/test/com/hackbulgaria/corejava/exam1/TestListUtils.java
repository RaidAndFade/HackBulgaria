package com.hackbulgaria.corejava.exam1;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;

public class TestListUtils {
    @Test
    public void testListReverse() {
        List<Integer> actuals = Arrays.asList(1, 2, 3, 4, 5, 6);
        List<Integer> expecteds = Arrays.asList(6, 5, 4, 3, 2, 1);
        assertEquals(expecteds, ListUtils.reverseList(actuals));
    }
    
    @Test
    public void testListSort() {
        List<Integer> actuals = Arrays.asList(5, 6, 4, 2, 3, 1);
        List<Integer> expecteds = Arrays.asList(1, 2, 3, 4, 5, 6);
        assertEquals(expecteds, ListUtils.sortList(actuals));
    }
}
