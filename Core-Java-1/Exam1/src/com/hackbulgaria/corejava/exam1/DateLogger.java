package com.hackbulgaria.corejava.exam1;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateLogger extends Logger {
    public DateLogger(int level) {
        super(level);
    }

    public DateLogger() {
        super();
    }

    @Override
    public void log(String message) throws InvalidLevelException {
        DateFormat currentDate = new SimpleDateFormat("HH:mm:ss yyyy-MM-dd");
        System.out.print(String.format("%s %d => ",  currentDate.format(new Date()), super.getLevel()));
        super.log(message);
    }
    
    @Override
    public void log(int level, String message) throws InvalidLevelException {
        if (super.getLevel() >= Logger.DEFAULT_LEVEL && level <= super.getLevel()) {
            this.log(message);
        }
    }
    
    public static void main(String[] args) throws InvalidLevelException {
        Logger logger = new DateLogger(3);
        logger.log("I see bad code.");
        logger.log("I might be wrong though.");
    }
}
