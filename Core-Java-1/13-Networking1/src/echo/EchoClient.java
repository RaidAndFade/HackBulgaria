package echo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class EchoClient {
    public static void main(String[] args) throws IOException {
        System.out.println("Enter <Host> <port>:");
        Scanner argIn = new Scanner(System.in);
        String hostName = argIn.next();
        int portNumber = argIn.nextInt();
        try (Socket echoSocket = new Socket(hostName, portNumber);
                PrintWriter outStream = new PrintWriter(echoSocket.getOutputStream(), true);
                BufferedReader inStream = new BufferedReader(new InputStreamReader(echoSocket.getInputStream()));
                BufferedReader consoleIn = new BufferedReader(new InputStreamReader(System.in));) {
            String userInput;
            while ((userInput = consoleIn.readLine()) != null) {
                outStream.println(userInput);
                System.out.println("Echo: " + inStream.readLine());
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
