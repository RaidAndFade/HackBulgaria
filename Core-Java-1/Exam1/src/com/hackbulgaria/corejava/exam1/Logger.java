package com.hackbulgaria.corejava.exam1;

public class Logger {
    private int level;
    public final static int DEFAULT_LEVEL = 3;

    public Logger(int level) {
        this.level = level;
    }

    public Logger() {
        this(DEFAULT_LEVEL);
    }

    protected int getLevel() {
        return this.level;
    }
    
    public void setLevel(int level) {
        if (level <= 0) {
            throw new InvalidLevelException("Importance level must be a positive number.");
        }
        this.level = level;
    }

    public void log(String message) {
        this.log(DEFAULT_LEVEL, message);
    }

    public void log(int level, String message) {
        if (this.level >= DEFAULT_LEVEL && level <= this.level) {
            System.out.println(message);
        } else {
            throw new InvalidLevelException("Importance level must be a positive number.");
        }
    }

    @SuppressWarnings("serial")
    public class InvalidLevelException extends RuntimeException {
        public InvalidLevelException() {
            super();
        }

        public InvalidLevelException(String message) {
            super(message);
        }
    }
}
