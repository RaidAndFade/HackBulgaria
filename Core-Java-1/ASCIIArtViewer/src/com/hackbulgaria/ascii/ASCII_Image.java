package com.hackbulgaria.ascii;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class ASCII_Image {
    private final int columns;
    private BufferedImage image;
    private int scale;

    public ASCII_Image(String file) throws IOException {
        this.columns = this.getTerminalMaxColumns();
        this.image = ImageIO.read(new File(file));
        this.scale = this.image.getWidth() > this.columns ? this.image.getWidth() / this.columns + 1 : 1;
    }

    public ASCII_Image(BufferedImage image) {
        this.columns = this.getTerminalMaxColumns();
        this.image = image;
        this.scale = this.image.getWidth() > this.columns ? this.image.getWidth() / this.columns + 1 : 1;
    }

    private int getTerminalMaxColumns() {
        return jline.Terminal.getTerminal().getTerminalWidth();
    }

    private String getCharacter(int intensity) {
        if (intensity >= 240) {
            return " ";
        } else if (intensity >= 200 && intensity < 240) {
            return ".";
        } else if (intensity >= 160 && intensity < 200) {
            return "*";
        } else if (intensity >= 120 && intensity < 160) {
            return "+";
        } else if (intensity >= 80 && intensity < 120) {
            return "...";
        } else if (intensity >= 40 && intensity < 80) {
            return "#";
        }
        return "@";
    }

    private int getIntensity(int x, int y) {
        Color color = new Color(this.image.getRGB(x, y), false);
        int intensity = (color.getRed() + color.getGreen() + color.getBlue()) / 3;
        return intensity;
    }

    private int getBlockAverageIntensity(int x, int y) {
        int averageIntensity = 0;
        for (int i = x; i < this.scale + x; i++) {
            for (int j = y; j < this.scale + y; j++) {
                averageIntensity += this.getIntensity(i, j);
            }
        }
        return averageIntensity / (this.scale * this.scale);
    }

    public void visualize() {
        String output = "";
        for (int y = 0; y < this.image.getHeight() - this.scale; y += this.scale) {
            for (int x = 0; x < this.image.getWidth() - this.scale; x += this.scale) {
                output += this.getCharacter(this.getBlockAverageIntensity(x, y));
            }
            output += "\n";
        }
        System.out.println(output);
    }
}
