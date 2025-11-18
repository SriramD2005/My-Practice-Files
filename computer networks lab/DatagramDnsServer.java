import java.net.*;
import java.io.*;
import java.util.*;

class DnsServer {
    byte[] send = new byte[1024];
    byte[] receive = new byte[1024];
    String[] dn = { "www.example.com", "www.gmail.com" };
    String[] ip = { "127.0.0.1", "196.3.5.2" };

    void serve() throws Exception {
        DatagramSocket server = new DatagramSocket(1333);
        DatagramPacket receiver = new DatagramPacket(receive, receive.length);
        server.receive(receiver);

        InetAddress clientAddress = receiver.getAddress();
        // we pass this to the constructor instead of passing in directly
        // because it returns the data in byte we type cast it by putting in the
        // constructor of string
        String name = new String(receiver.getData());
        for (int i = 0; i < ip.length; i++) {
            if (dn[i].equals(name.trim())) {
                send = ip[i].getBytes();
                DatagramPacket Sender = new DatagramPacket(send, send.length, clientAddress, receiver.getPort());
                server.send(Sender);
                break;
            }

        }
    }
}

public class DatagramDnsServer {
    public static void main(String args[]) throws Exception {
        DnsServer s = new DnsServer();
        s.serve();
    }
}