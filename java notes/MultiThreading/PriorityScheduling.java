package MultiThreading;
import java.lang.Thread;
//MAX_PRIORITY = 10
//MIN_PRIORITY = 1
//NORM_PRIORITY = 5(default if priority not set)
public class PriorityScheduling {
    public static void main(String args[]){
        Thread t2 = new Thread2();
        Thread1 t1 = new Thread1();
        Thread3 t3 = new Thread3();
        t1.setPriority(Thread.MAX_PRIORITY);
        t2.setPriority(Thread.MIN_PRIORITY);
        t3.setPriority(t2.getPriority()+2);
        DThread dT = new DThread();
        dT.start();
        t1.start();
        t2.start();
        t3.start();
    }
}
class Thread1 extends Thread{
    public void run(){
        for (int i = 0; i<5; i++){
            System.out.println("thread 1:"+i);
        }
        System.out.println("thread 1 complete");
    }
}
class Thread2 extends Thread{
    public void run(){
        for (int i = 0; i<5; i++){
            System.out.println("thread 2:"+i);
        }
        System.out.println("thread 2 complete");

    }
} 
class Thread3 extends Thread{
    public void run(){
        for (int i = 0; i<5; i++){
            System.out.println("thread 3:"+i);
        }
        System.out.println("thread 3 complete");

    }
}
/*Daemon threads are that has lowest priority that run in the background and do tasks like garbage collection,
periodic check, they will be shut by the JVM in the end of a program(Process)*/
class DThread extends Thread{
    public void run(){
        for (int i = 0; i<5; i++){
            System.out.println("Daemon thread:"+i);
        }
        System.out.println("Daemon thread complete");

    }
}