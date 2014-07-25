import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class RBI_Protocol {
    private static final int DEFAULT_PORT = 1234;
    private static final String DEFAULT_EOM = "<[?!EOM!?]>";
    public static int PORT = DEFAULT_PORT;
    public static String EOM = DEFAULT_EOM;

    public static String read(Socket socket) throws IOException {
        String outputString = "";
        BufferedReader inStream = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        String line;
        while (true) {
            line = inStream.readLine();
            if (line == null || line.contains(EOM)){
                break;
            }
            outputString += line + "\n";
        }
        return outputString;
    }

    public static void write(Socket socket, String message) throws IOException {
        PrintWriter outStream = new PrintWriter(socket.getOutputStream(), true);
        outStream.println(message);
        outStream.println(EOM);
    }
}
