package MultiThreading;
import java.lang.Thread;
public class RaceCondition extends Thread{
    static int x = 0;
    static int count = 0;
    static RaceCondition threadArray[] = new RaceCondition[10000];
    public void run(){
        x = x+1;
        //x = x-1;
        count++;
    }
    public static void main(String args[])throws InterruptedException{
        for (int i = 0; i<10000; i++){
            threadArray[i] = new RaceCondition();
            threadArray[i].start();
        }
        for (int i = 0; i<10000; i++){
            threadArray[i].join();
        }
        System.out.println("x:"+x+"\tcount:"+count);
    }
}
