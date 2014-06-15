package com.hackbulgaria.corejava.exam1;

public class Logger {
    private int level;

    public Logger(int level) {
        this.level = level;
    }

    public Logger() {
        this(3);
    }

    protected int getLevel() {
        return this.level;
    }
    
    public void setLevel(int level) throws InvalidLevelException {
        if (level <= 0) {
            throw new InvalidLevelException();
        }
        this.level = level;
    }

    public void log(String message) {
        if (this.level >= 3) {
            System.out.println(message);
        }
    }

    public void log(int level, String message) {
        if (this.level >= 3 && level <= this.level) {
            System.out.println(message);
        }
    }

    @SuppressWarnings("serial")
    class InvalidLevelException extends Exception {
        public InvalidLevelException() {
            super();
        }

        public InvalidLevelException(String message) {
            super(message);
        }
    }
}
