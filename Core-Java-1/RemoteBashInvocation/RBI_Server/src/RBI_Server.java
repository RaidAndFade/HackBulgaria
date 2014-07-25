import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class RBI_Server {
    public static void main(String[] args) {
        int portNumber = RBI_Protocol.PORT;
        System.out.println(timestampMsg("Server started!"));
        try (ServerSocket servSocket = new ServerSocket(portNumber); Socket clientSocket = servSocket.accept()) {
            System.out.println(timestampMsg("Client connected!"));
            while (true) {
                String command = RBI_Protocol.read(clientSocket);
                try {
                    Process process = Runtime.getRuntime().exec(command);
                    long startTime = System.currentTimeMillis();
                    process.waitFor();
                    long endTime = System.currentTimeMillis();
                    BufferedReader bfReader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    String output = "";
                    String line;
                    while ((line = bfReader.readLine()) != null) {
                        output += line + "\n";
                    }
                    RBI_Protocol.write(clientSocket, output);
                    long totalTime = endTime - startTime;
                    // replaces multiple spaces with just 1 space for better readability
                    String commandTotalTime = String.format("Command %s executed in %d ms", command.replaceAll("\\s+", " "), totalTime);
                    System.out.println(timestampMsg(commandTotalTime));
                // catches empty commands, but doesn't kill the server
                } catch (ArrayIndexOutOfBoundsException | IllegalArgumentException e) {
                } catch (InterruptedException e) {
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String timestampMsg(String input) {
        Calendar calendar = Calendar.getInstance();
        SimpleDateFormat dateFormatter = new SimpleDateFormat("HH:mm:ss");
        String time = dateFormatter.format(calendar.getTime());
        return String.format("[%s] %s", time, input);
    }
}
