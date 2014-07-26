import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

public class JavaFileDownloader {
    public static void download(String downloadFrom, String saveAs) throws IOException {
        URL link = new URL(downloadFrom);
        long startTime = System.currentTimeMillis();
        InputStream in = new BufferedInputStream(link.openStream());
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        byte[] buf = new byte[1024];
        int n = 0;
        while (-1 != (n = in.read(buf))) {
            out.write(buf, 0, n);
        }
        out.close();
        in.close();
        byte[] response = out.toByteArray();

        FileOutputStream fos = new FileOutputStream(saveAs);
        fos.write(response);
        fos.close();
        long endTime = System.currentTimeMillis();
        long totalTime = endTime - startTime;
        System.out.println(String.format("Downloaded %s for %d ms\nAnd saved as %s", downloadFrom, totalTime, saveAs));
    }
}
