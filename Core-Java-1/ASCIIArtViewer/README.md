# ASCII Art Viewer

## Purpose:
Prints images in the console as ASCII art.
Gifs can have a custom delay between frames.
Support for videos soon. (No documentation for the library I'm planning to use...)

**Supported formats**:
* jpg
* png
* gif
* bmp
* wbmp



## How to run:
If you want the whole repo
```
git clone git@github.com:syndbg/HackBulgaria.git
cd HackBulgaria/Core-Java-1/ASCIIArtViewer/
java -jar build/asciiViewer.jar
```

If you want only the jar
```
wget https://github.com/syndbg/HackBulgaria/blob/master/Core-Java-1/ASCIIArtViewer/build/asciiViewer.jar?raw=true -O asciiViewer.jar
java -jar asciiViewer.jar
```

## Third-party libraries used:
* [jline 1.0](http://jline.sourceforge.net/)
* [apache.commons.io 2.4](http://commons.apache.org/proper/commons-io/)
