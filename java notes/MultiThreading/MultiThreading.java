package MultiThreading;
import java.lang.Thread;
public class MultiThreading {
    public static void main(String args[]){
        Thread a = new threadA();
        threadB b = new threadB();
        threadC c = new threadC();
        System.out.println(Thread.MAX_PRIORITY);
        a.start();
        b.start();
        c.start();
        try{
            a.join();
            System.out.println("joined a");
        }
        catch (InterruptedException e){
            System.out.println(e.getMessage());
        }
        System.out.println("main method is over...");
    }
}
class threadA extends Thread{
    public void run(){
        for (int i = 1;i<=5;i++){
            System.out.println("threadA:"+ -i);
        }
        System.out.println("threadA completed");
    }
}
class threadB extends Thread{
    public void run(){
        for (int i = 1;i<=5;i++){
            System.out.println("threadB:"+i*i);
        }
        System.out.println("threadB completed");
    }
}
class threadC extends Thread{
    public void run(){
        for (int i = 1;i<=5;i++){
            System.out.println("threadC:"+2*i);
        }
        System.out.println("threadC is completed");
    }
}