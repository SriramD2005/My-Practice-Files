package MultiThreading;
import java.lang.Thread;
public class RunnableInterface {
    Thread t1 = new Thread(new Threads());
    public static void main(String args[]){
        //this.t1.start(); -> a static method can not access the object's variables.
        RunnableInterface ri = new RunnableInterface();
        ri.t1.start();
    }
    int x(){
        t1.start();
        return 0;
    }
}
class Threads implements Runnable{
    public void run(){
        System.out.println("Running");
    }
}