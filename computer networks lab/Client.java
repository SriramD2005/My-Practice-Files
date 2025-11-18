import java.net.*;
import java.io.*;
public class Client{
    BufferedReader con = new BufferedReader(new InputStreamReader(System.in));
    String line;
    void request(){
        try{
            Socket s = new Socket("localhost",9999);
            BufferedReader r = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter w = new PrintWriter(s.getOutputStream(),true);
        do{
            line = r.readLine();
            System.out.println("Server says :"+line);
            line = con.readLine();
            w.println(line);
            w.flush();
        }
        while (!line.equals("bye"));
    }
    catch(Exception e){
        System.err.println(e);
    }
}
    public static void main(String args[]){
        Client c = new Client();
        c.request();
    }
}


