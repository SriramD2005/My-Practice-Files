import java.net.*;
import java.io.*;
public class cS {
    public static void main(String args[])throws Exception{
        client c = new client();
        c.run();
    }
}
class client {
    DatagramSocket clsocket;
    BufferedReader br;
    void run() throws Exception{
        byte[] send = new byte[1024];
        byte[] receive = new byte[1024];
        clsocket = new DatagramSocket(1000);
        br = new BufferedReader(new InputStreamReader(System.in));
        DatagramPacket receiver = new DatagramPacket(receive, receive.length);
        DatagramPacket sender;
        InetAddress addr;
        String line;
        do{
            clsocket.receive(receiver);
            line = new String(receiver.getData());
            addr = receiver.getAddress();
            System.out.println("Server:"+line);
            System.out.print("client:");
            line = br.readLine();
            send = line.getBytes();
            sender = new DatagramPacket(send, send.length, addr, receiver.getPort());
            clsocket.send(sender);
        }
        while (!line.trim().equals("bye"));
    }
}