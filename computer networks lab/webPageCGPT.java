import java.io.*;
import java.net.*;
public class webPageCGPT {
    public static void main(String args[]) throws Exception{
        URI uri = new URI("http", "httpforever.com", null);
        URL url = uri.toURL();
        String hostname = url.getHost();
        Socket s = new Socket(hostname, 80);

        // Send an HTTP GET request
        BufferedWriter requestWriter = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
        requestWriter.write("GET / HTTP/1.1\r\n");
        requestWriter.write("Host: " + hostname + "\r\n");
        requestWriter.write("Connection: close\r\n");
        requestWriter.write("\r\n");
        requestWriter.flush();

        // Read the response
        BufferedReader webreader = new BufferedReader(new InputStreamReader(s.getInputStream()));
        BufferedWriter fileWriter = new BufferedWriter(new FileWriter("googlepage.html"));
        String line;
        while ((line = webreader.readLine()) != null) {
            System.out.println(line);
            fileWriter.write(line);
            fileWriter.newLine(); // Add a newline to preserve formatting
        }

        // Close resources
        webreader.close();
        fileWriter.close();
        s.close();
    }
}