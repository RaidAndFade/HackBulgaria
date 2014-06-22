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
    
    public void setLevel(int level) throws InvalidLevelException {
        if (level <= 0) {
            throw new InvalidLevelException("Importance level must be a positive number.");
        }
        this.level = level;
    }

    public void log(String message) throws InvalidLevelException {
        if (this.level >= 3) {
            System.out.println(message);
        } else {
            throw new InvalidLevelException("Importance level must be a positive number.");
        }
    }

    public void log(int level, String message) throws InvalidLevelException {
        if (this.level >= DEFAULT_LEVEL && level <= this.level) {
            System.out.println(message);
        } else {
            throw new InvalidLevelException("Importance level must be a positive number.");
        }
    }

    @SuppressWarnings("serial")
    public class InvalidLevelException extends Exception {
        public InvalidLevelException() {
            super();
        }

        public InvalidLevelException(String message) {
            super(message);
        }
    }
}
