public class interfaces3 {
    Runable 
}
interface Runable{
    int x = 10;
    void run();
}
class runner implements Runable{
    void run(){
        System.out.println("running"+x);
    }
}