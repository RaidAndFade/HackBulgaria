package com.hackbulgaria.oop.calculator;

import java.util.EmptyStackException;
import java.util.Stack;

public class Calculator {
    public static void calculate(String expression) {
        expression = expression.replaceAll("\\s+", "");
        Stack<Integer> numstack = new Stack<Integer>();
        Stack<Character> opstack = new Stack<Character>();
        int pos = 0;
        try {
            while (pos < expression.length()) {
                char ch = expression.charAt(pos);
                pos += 1;
                if (isOperator(ch)) {
                    if (opstack.size() == 0) {
                        opstack.push(ch);
                    } else {
                        char previousOp = opstack.pop();
                        if (precedence(ch) > precedence(previousOp)) {
                            opstack.push(previousOp);
                        } else {
                            evaluateTop(numstack, previousOp);
                        }
                        opstack.push(ch);
                    }
                } else if (ch == '(') {
                    opstack.push(ch);
                } else if (ch == ')') {
                    boolean done = false;
                    while (!done) {
                        if (opstack.size() == 0) {
                            printError("No matching");
                        }
                        char previousOp = opstack.pop();
                        if (previousOp == '(') {
                            done = true;
                        } else {
                            evaluateTop(numstack, previousOp);
                        }
                    }
                } else if (Character.isDigit(ch)) {
                    int start = pos - 1;
                    while (pos < expression.length() && Character.isDigit(expression.charAt(pos))) {
                        pos += 1;
                    }
                    String number = expression.substring(start, pos);
                    numstack.push(Integer.parseInt(number));
                } else {
                    printError("Number, operator or parenthesis expected.");
                }
            }
            while (opstack.size() > 0) {
                char previousOp = opstack.pop();
                if (previousOp == '(') {
                    printError("No matching");
                } else {
                    evaluateTop(numstack, previousOp);
                }
            }
        } catch (EmptyStackException e) {
            printError("Invalid expression");
        }

        // Misses some cases, try/catch is better..?
        //        if (numstack.size() == 0) {
        //            printError("Invalid expression");
        //        }
        System.out.println(numstack.pop());
        if (numstack.size() > 0) {
            printError("Invalid expression");
        }
    }

    public static boolean isOperator(char ch) {
        return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '!' || ch == '^';
    }

    public static void printError(String message) {
        System.out.println("ERROR! " + message);
        System.exit(1);;
    }

    public static int precedence(char ch) {
        if (ch == '+' || ch == '-') {
            return 1;
        } else if (ch == '*' || ch == '/' || ch == '^') {
            return 2;
        } else if (ch == '!') {
            return 3;
        } else {
            return 0;
        }
    }

    public static void evaluateTop(Stack<Integer> stack, char operator) {
        if (stack.size() == 0) {
            printError("Invalid expression");
        }
        int y = stack.pop();
        if (stack.size() == 0 && operator != '!') {
            printError("Invalid expression");
        }
        int x = 0;
        if (operator != '!') {
            x = stack.pop();
        }
        int z = 0;
        if (operator == '*') {
            z = x * y;
        } else if (operator == '/') {
            if (y == 0) {
                printError("Divide by 0");
            } else {
                z = x / y;
            }
        } else if (operator == '+') {
            z = x + y;
        } else if (operator == '-') {
            z = x - y;
        } else if (operator == '!') {
            z = 1;
            for (int i = 1; i <= y; i++) {
                z *= i;
            }
        } else if (operator == '^') {
            z = (int) Math.pow(x, y);
        } else {
            printError("Syntax error");
        }
        stack.push(z);
    }
}
