import java.io.*;
import java.net.*;
class webPageDownload{
    public static void main(String args[]) throws Exception{
    URI uri = new URI("http","www.google.com",null);
    URL url= uri.toURL();
    String hostname = url.getHost();
    Socket s = new Socket(hostname, 80);
    BufferedWriter connRequest = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
    connRequest.write("Get / HTTP/1.1\r\n");
    connRequest.write("Host: "+hostname+"\r\n");
    connRequest.write("Connectiion: close\r\n");
    connRequest.write("\r\n");
    connRequest.flush();
    BufferedReader webreader=new BufferedReader(new InputStreamReader((s.getInputStream())));
    BufferedWriter fileWriter=new BufferedWriter(new FileWriter("googelpage"));
    String line;
    while ((line=webreader.readLine())!=null){
        System.out.println(line);
        fileWriter.write(line);
    }
}}