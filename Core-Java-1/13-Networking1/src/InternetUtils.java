import java.io.IOException;
import java.net.Inet4Address;
import java.net.Inet6Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.Collections;
import java.util.Enumeration;
import java.util.Scanner;

public class InternetUtils {
    public static void main(String[] args) throws SocketException {
        Scanner consoleIn = new Scanner(System.in);
        System.out.print("1)Print your IPv4 address\n2)Print your IPv6 adress\n3)Print reachable IPv4 hosts: ");
        int choice = consoleIn.nextInt();
        consoleIn.close();
        if (choice == 1 || choice == 2) {
            String protocolVersion = choice == 1 ? "IPv4" : "IPv6";
            InetAddress address = getWLANipAddress(protocolVersion);
            System.out.println(address != null ? address : protocolVersion
                    + " address not found. Is your internet down?");
        } else if (choice == 3) {
            InetAddress address = getWLANipAddress("IPv4");
            if (address != null) {
                printReachableHosts(address);
            } else {
                System.out.println("IPv4 Address not found. Is your internet down?");
            }
        } else {
            System.out.println("Unknown choice.");
        }
    }

    public static InetAddress getWLANipAddress(String protocolVersion) throws SocketException {
        Enumeration<NetworkInterface> nets = NetworkInterface.getNetworkInterfaces();
        for (NetworkInterface netint : Collections.list(nets)) {
            if (netint.isUp() && !netint.isLoopback() && !netint.isVirtual()) {
                Enumeration<InetAddress> inetAddresses = netint.getInetAddresses();
                for (InetAddress inetAddress : Collections.list(inetAddresses)) {
                    if (protocolVersion.equals("IPv4")) {
                        if (inetAddress instanceof Inet4Address) {
                            return inetAddress;
                        }
                    } else {
                        if (inetAddress instanceof Inet6Address) {
                            return inetAddress;
                        }
                    }
                }
            }
        }
        return null;
    }

    public static void printReachableHosts(InetAddress inetAddress) throws SocketException {
        String ipAddress = inetAddress.toString();
        ipAddress = ipAddress.substring(1, ipAddress.lastIndexOf('.')) + ".";
        for (int i = 0; i < 256; i++) {
            String otherAddress = ipAddress + String.valueOf(i);
            try {
                if (InetAddress.getByName(otherAddress.toString()).isReachable(50)) {
                    System.out.println(otherAddress);
                }
            } catch (UnknownHostException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
