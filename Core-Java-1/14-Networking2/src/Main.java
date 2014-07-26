import java.util.Scanner;

import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

public class Main {
    static final String DEFAULT_FILENAME = "lack_of_creativity";

    public static void main(String[] args) {
        System.out.print("1) Download, 2) Web crawl: ");
        Scanner consoleIn = new Scanner(System.in);
        int option = consoleIn.nextInt();
        JFileChooser fileChooser = new JFileChooser();
        try {
            if (option == 1) {
                String url = JOptionPane.showInputDialog(null, "Download from URL: ");
                String fileName = DEFAULT_FILENAME;
                if (fileChooser.showSaveDialog(null) == JFileChooser.APPROVE_OPTION) {
                    fileName = fileChooser.getSelectedFile().getAbsolutePath();
                }
                JavaFileDownloader.download(url, fileName);
            } else if (option == 2) {
                String url = JOptionPane.showInputDialog(null, "Web crawl in URL: ");
                String needle = JOptionPane.showInputDialog(null, "Needle: ");
                WebsiteCrawler crawler = new WebsiteCrawler();
                crawler.crawl(url, needle);
            } else {
                System.out.println("Unknown choice");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        consoleIn.close();
    }
}
