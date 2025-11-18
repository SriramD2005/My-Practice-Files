import java.lang.*;
import java.io.*;
class MyException extends Exception{
    MyException(String s){
        super(s);//calling the costructor of the super class(here Exception)
    }
}
public class userDefinedException {
    public static void main(String args[]){

        try{
            BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
            int x = Integer.valueOf(r.readLine());
            int y = Integer.valueOf(r.readLine());
            double z = (double) x/y;
            if (z<1) throw new MyException("very small divident");
        }
        catch (MyException e){
            System.out.println(e.getMessage());
        }
        catch (IOException e){
            System.out.println(e.getMessage());
        }
    }
}
