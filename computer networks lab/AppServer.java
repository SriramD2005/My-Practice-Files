
//package ChatApplication;
import java.io.*;
import java.net.*;

public class AppServer {
    int port;

    AppServer(int port) {
        this.port = port;
    }

    void serve() {
        try {
            ServerSocket s = new ServerSocket(port);
            System.out.println("Server is running");
            Socket serversClient = s.accept();
            BufferedReader r = new BufferedReader(new InputStreamReader(serversClient.getInputStream()));
            PrintWriter w = new PrintWriter(serversClient.getOutputStream(), true);
            BufferedReader con = new BufferedReader((new InputStreamReader(System.in)));
            String line;
            w.println("Hello dear client, say bye to finish");
            w.flush();
            do {
                line = r.readLine();
                System.out.println("client:" + line);
                line = con.readLine();
                w.println(line);
                w.flush();
            } while (!line.equals("bye"));
            s.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public static void main(String args[]) {
        AppServer s = new AppServer(9897);
        s.serve();
    }
}
// helloWorld - lower - object/variables, method
// HelloWorld - upper - class/namespace, type
