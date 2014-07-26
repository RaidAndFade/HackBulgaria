import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.LinkedList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class WebsiteCrawler {
    private List<URL> visitedUrls;

    public WebsiteCrawler() {
        this.visitedUrls = new LinkedList<URL>();
    }

    public void crawl(String url, String needle) throws IOException {
        this.crawl(new URL(url), needle);
    }

    public void crawl(URL url, String needle) throws IOException {
        String currentPage = getURLcontents(url);
        if (currentPage.contains(needle)) {
            System.out.println(url.toString());
        } else {
            for (String link : getAllLinks(currentPage)) {
                if (!link.contains("index.html") && !link.contains("http://") && !link.contains("https://")) {
                    URL toBeVisited = new URL(String.format("%s%s", url.toString(), link));
                    if (!this.visitedUrls.contains(toBeVisited)) {
                        this.crawl(toBeVisited, needle);
                    }
                    this.visitedUrls.add(toBeVisited);
                }
            }
        }
    }

    private static String getURLcontents(URL url) throws IOException {
        StringBuilder output = new StringBuilder();
        BufferedReader urlReader = new BufferedReader(new InputStreamReader(url.openStream()));
        String line;
        while ((line = urlReader.readLine()) != null) {
            output.append(line + "\n");
        }
        return output.toString();
    }

    private static List<String> getAllLinks(String content) {
        List<String> resultList = new LinkedList<>();
        String regex = "<a.*?href=\"((?!javascript).*?)\".*?>";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(content);
        while (matcher.find()) {
            resultList.add(matcher.group(1));
        }
        return resultList;
    }
}
