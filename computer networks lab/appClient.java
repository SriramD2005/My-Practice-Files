import java.io.*;
import java.net.*;
class appClient{
    public static void main(String args[]) throws Exception{
        Socket s = new Socket("127.0.0.1",9897);
        BufferedReader r = new BufferedReader(new InputStreamReader((s.getInputStream())));
        BufferedReader con = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter w = new PrintWriter(s.getOutputStream());
        String line;
        do{
            line = r.readLine();
            System.out.println("server:"+line);
            line = con.readLine();
            w.println(line);
            w.flush();
        } 
        while(!line.equals("bye"));
     }
}