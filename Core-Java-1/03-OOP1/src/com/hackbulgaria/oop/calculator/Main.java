package com.hackbulgaria.oop.calculator;

public class Main {
    public static void main(String[] args) {
        Console consoleIn = new Console();
        String userInput;
        while (true) {
            userInput = consoleIn.readLine("Expression: ");
            Calculator.calculate(userInput);
        }
    }
}
