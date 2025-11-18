import java.io.*;
import java.net.*;
class Server{
    int port;
    private ServerSocket server;
    Server(int port){
        this.port = port;
    
    try{
        this.server = new ServerSocket(port);
    }
    catch(Exception e){
        System.out.println(e);
    }}
    public void serve(){
        try{
            Socket client = server.accept();
            while(true){
                System.out.println("Server is on");
                
                BufferedReader r = new BufferedReader(new InputStreamReader(client.getInputStream()));
                PrintWriter w = new PrintWriter(client.getOutputStream(),true);
                w.write("hello dear client"+"\n say bye to end");
                w.flush();
                String line;
                do{
                    line = r.readLine();
                    System.out.println("from you client:"+line);
                    w.println();
                }
                while (!line.equals("bye"));
                client.close();
                }
        }
        catch (Exception e){
            System.err.println(e);
        }
        }
}
class ClientServer{
    public static void main(String args[]){
        Server myserver = new Server(9999);
        myserver.serve();
    }
}