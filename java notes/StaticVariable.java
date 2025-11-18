public class StaticVariable {
    public static void main(String args[]){
        Example e = new Example();
        e.x = 23;
        Example e2 = new Example();
        e2.printX();
    }
}
class Example{
    static int x;
    void printX(){
        System.out.println(x);
    }
}