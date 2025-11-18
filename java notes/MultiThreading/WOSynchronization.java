package MultiThreading;
import java.lang.Thread;
public class WOSynchronization{//WO means without
    public static void main(String args[]){
        Withdraw w = new Withdraw(50);
        Thread t1 = new Thread(w);
        Thread t2 = new Thread(w);
        t1.start();
        t2.start();
        try{
        t1.join();
        t2.join();}
        catch(InterruptedException e){
            System.out.println(e);
        }
        System.out.println("balance:"+w.balance);
    }
}
class Withdraw implements Runnable{
    int balance = 50;
    int amt;
    Withdraw(int amt){
        this.amt = amt;
    }
    void withdraw(int amt){
        if (amt <= balance){
            try{
                Thread.sleep(100);
            }
            catch(InterruptedException e){
                System.out.println(e);
            }
            balance -= amt;
        }
        else{
            System.err.println("no enough balance, current balance = "+balance);
        }
    }
    public void run(){
        withdraw(amt);
    }
    
}