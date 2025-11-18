import java.net.*;
import java.util.Scanner;

public class PrivyLinkUdpResponder {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket(4449);
        socket.setReuseAddress(true);
        byte[] buf = new byte[1024];
        Scanner scanner = new Scanner(System.in);
        System.out.println("Responder listening on 4449");
        while (true) {
            DatagramPacket p = new DatagramPacket(buf, buf.length);
            socket.receive(p);
            String msg = new String(p.getData(), 0, p.getLength());
            System.out.println(p.getAddress().getHostAddress() + ":" + p.getPort() + " -> " + msg);
            System.out.print("Reply: ");
            String reply = scanner.nextLine();
            byte[] replyBytes = reply.getBytes();
            DatagramPacket resp = new DatagramPacket(replyBytes, replyBytes.length, p.getAddress(), p.getPort());
            socket.send(resp);
            // clear buffer (not strictly necessary because we use length)
        }
    }
}