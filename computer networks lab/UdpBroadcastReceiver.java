import java.net.*;
import java.util.Scanner;
public class UdpBroadcastReceiver {
    public static void main(String args[]){
        try{
            DatagramSocket socket = new DatagramSocket(4446);
            byte[] buffer = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            String reply = "none";
            Scanner scanner = new Scanner(System.in);
            while(!reply.equals("stop")){
                socket.receive(packet);
                String msg = new String(packet.getData(), 0, packet.getLength());
                System.out.println("Received: " + msg);
                // Respond to sender
                
                reply = scanner.nextLine();
                InetAddress senderAddress = packet.getAddress();
                int senderPort = packet.getPort();
                DatagramPacket response = new DatagramPacket(reply.getBytes(), reply.length(), senderAddress, senderPort);
                socket.send(response);
            }
            socket.close();
            scanner.close();
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }
}