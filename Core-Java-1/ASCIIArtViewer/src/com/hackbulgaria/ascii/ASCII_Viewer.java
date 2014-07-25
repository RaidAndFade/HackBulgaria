package com.hackbulgaria.ascii;

import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;

import javax.imageio.ImageIO;

import org.apache.commons.io.FilenameUtils;

public class ASCII_Viewer {
    HashSet<String> imageFormats = new HashSet<String>(Arrays.asList(ImageIO.getReaderFormatNames()));

    public ASCII_Viewer(String file, int frameDelay) throws InterruptedException, IOException {
        String extension = FilenameUtils.getExtension(file);
        if (extension.equals("gif")) {
            new ASCII_Gif(file, frameDelay).visualize();
        } else if (this.imageFormats.contains(extension)) {
            new ASCII_Image(file).visualize();
            ;
        }
    }
}
