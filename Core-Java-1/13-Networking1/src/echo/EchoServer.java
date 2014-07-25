package echo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class EchoServer {
    public static void main(String[] args) {
        System.out.println("Usage: <port number>");
        Scanner consoleIn = new Scanner(System.in);
        int portNumber = consoleIn.nextInt();

        try (ServerSocket serverSocket = new ServerSocket(portNumber);
                Socket clientSocket = serverSocket.accept();
                PrintWriter outStream = new PrintWriter(clientSocket.getOutputStream(), true);
                BufferedReader inStream = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()))) {
            String inputLine;
            while ((inputLine = inStream.readLine()) != null) {
                outStream.println(inputLine);
                System.out.println(inputLine);
            }
        } catch (IOException e) {
            System.out.println("Exception caught when trying to listen on port " + portNumber
                    + " or listening for a connection");
            System.out.println(e.getMessage());
        }
    }
}
