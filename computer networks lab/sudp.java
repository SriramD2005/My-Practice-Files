import java.io.*;
import java.net.*;
public class sudp {
    public static void main(String args[])throws Exception{
    server s = new server();
    s.serve();
}}
class server{
    DatagramSocket Ssocket;
    BufferedReader br;
    void serve() throws Exception{
        byte[] send = new byte[1024];
        byte[] receive = new byte[1024];
        Ssocket = new DatagramSocket(9999);
        br = new BufferedReader(new InputStreamReader(System.in));
        DatagramPacket receiver = new DatagramPacket(receive, receive.length);
        DatagramPacket sender;
        InetAddress addr;
        String line;
        send = "hello server".getBytes();
        addr = InetAddress.getByName("127.0.0.1");
        sender = new DatagramPacket(send, send.length, addr, 1000);
        Ssocket.send(sender);
        do{
           Ssocket.receive(receiver);
           line = new String(receiver.getData());
           addr = receiver.getAddress();
           System.out.println("client:"+line);
           System.out.print("server:"); 
           line = br.readLine();
           send = line.getBytes();
           sender = new DatagramPacket(send, send.length, addr, receiver.getPort());
           Ssocket.send(sender);
        }
        while(!line.equals("bye"));
}
}