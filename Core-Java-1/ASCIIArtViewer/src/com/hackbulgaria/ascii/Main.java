package com.hackbulgaria.ascii;

import java.io.IOException;
import java.util.Scanner;

import javax.swing.JFileChooser;
import javax.swing.JFrame;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        final JFileChooser fileChooser = new JFileChooser();
        String filePath = "";
        Scanner consoleIn = new Scanner(System.in);
        if (fileChooser.showOpenDialog(new JFrame()) == JFileChooser.APPROVE_OPTION) {
            filePath = fileChooser.getSelectedFile().getAbsolutePath();
        } else {
            System.out.print("File path: ");
            try {
                filePath = consoleIn.nextLine().trim();
            } catch (Exception e) {
                System.out.println("Invalid file path");
                e.printStackTrace();
            }
        }
        System.out.print("Frame delay(0 for default): ");
        int frameDelay = consoleIn.nextInt();
        consoleIn.close();

        @SuppressWarnings("unused")
        ASCII_Viewer viewer = new ASCII_Viewer(filePath, frameDelay);
    }
}
