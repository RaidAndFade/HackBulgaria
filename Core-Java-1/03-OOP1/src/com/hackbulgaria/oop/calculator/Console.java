package com.hackbulgaria.oop.calculator;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Console {
    private BufferedReader reader;

    public String readLine(String prompt) {
        System.out.print(prompt);
        try {
            final String result = this.bufferedReader().readLine();
            System.out.println(); //add a new line
            return result;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    private BufferedReader bufferedReader() {
        return this.reader == null ? (this.reader = new BufferedReader(new InputStreamReader(System.in))) : this.reader;
    }
}
