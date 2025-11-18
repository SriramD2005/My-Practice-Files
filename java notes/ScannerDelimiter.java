import java.util.Scanner;
public class ScannerDelimiter {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter(";");
        while (true){
            String in = sc.next();
            if (in.trim().equals("bye")){
                System.out.println("Bye");
                break;
            }
            System.out.println(in);
        }
    }
}
