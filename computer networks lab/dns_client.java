import java.net.*;
import java.io.*;
public class dns_client {
   public static void main(String args[])throws Exception{
    Client c = new Client();
    c.run();
   } 
}
class Client{
    byte[] send = new byte[1024];
    byte[] receive = new byte[1024];
    void run()throws Exception{
        DatagramSocket s = new DatagramSocket(7896);
        BufferedReader con = new BufferedReader(new InputStreamReader(System.in));
        String line;
        DatagramPacket sendpack, receipack;
        do{
            line = con.readLine();
            send = line.getBytes();
            InetAddress serverAddress = InetAddress.getByName("127.0.0.1");
            sendpack = new DatagramPacket(send, send.length, serverAddress, 1333);
            receipack = new DatagramPacket(receive, receive.length);
            s.send(sendpack);
            System.out.println("waiting for server message");
            s.receive(receipack);
            String data = new String(receipack.getData());
            System.out.println("the ip address is: "+data);
        }
        while (!line.equals("bye"));
    }
}