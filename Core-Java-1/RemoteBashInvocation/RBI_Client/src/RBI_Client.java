import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class RBI_Client {
    public static void main(String[] args) {
        String hostName = "";
        if (args.length < 1) {
            System.out.print("Hostname: ");
            // shouldn't be closed
            @SuppressWarnings("resource")
            Scanner consoleIn = new Scanner(System.in);
            hostName = consoleIn.next();
        } else {
            hostName = args[0];
        }
        int portNumber = RBI_Protocol.PORT;
        try (Socket socket = new Socket(hostName, portNumber);
                BufferedReader consoleIn = new BufferedReader(new InputStreamReader(System.in));) {
            System.out.println("Connected!");
            String message = "";
            while (!message.equals("q")) {
                System.out.print(">");
                message = consoleIn.readLine();
                RBI_Protocol.write(socket, message);
                System.out.println(RBI_Protocol.read(socket));
            }
        } catch (UnknownHostException e) {
            System.err.println("Don't know about host " + hostName);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " + hostName);
            System.exit(1);
        }
    }
}
