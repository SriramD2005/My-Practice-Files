package MultiThreading;
import java.lang.Thread;
public class MultiThreading2 {
    public static void main(String args[]){
        Thread1 a = new Thread1();
        Thread2 b = new Thread2();
        a.run();
        b.run();
    }
}
class Thread1 extends Thread{
    public void run(){
        for (int i = 1;i<=5;i++){
            System.out.println("thread1:"+ -i);
        }
        System.out.println("thread1 completed");
    }
}
class Thread2 extends Thread{
    public void run(){
        for (int i = 1;i<=5;i++){
            System.out.println("thread2:"+i*i);
        }
        System.out.println("thread2 completed");
    }
    }
