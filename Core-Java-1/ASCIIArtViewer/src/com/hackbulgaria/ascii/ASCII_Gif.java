package com.hackbulgaria.ascii;

import java.io.IOException;
import java.util.LinkedList;
import java.util.List;

import jline.ConsoleReader;

public class ASCII_Gif {
    private static final int DEFAULT_FRAME_DELAY = 50;
    private int frameDelay = DEFAULT_FRAME_DELAY;
    private List<String> renderedFrames;

    public ASCII_Gif(String file, int frameDelay) {
        this.frameDelay = frameDelay;
        this.renderedFrames = this.renderGifFrames(file);
    }

    private List<String> renderGifFrames(String file) {
        List<String> list = new LinkedList<String>();
        GifDecoder decoder = new GifDecoder();
        decoder.read(file);
        for (int i = 0; i < decoder.getFrameCount(); i++) {
            ASCII_Image frame = new ASCII_Image(decoder.getFrame(i));
            list.add(frame.toString());
        }
        return list;
    }

    public void visualize() throws InterruptedException, IOException {
        ConsoleReader reader = new ConsoleReader();
        for (String renderedFrame : this.renderedFrames) {
            System.out.println(renderedFrame);
            Thread.sleep(this.frameDelay);
            reader.clearScreen();
        }
    }
}
