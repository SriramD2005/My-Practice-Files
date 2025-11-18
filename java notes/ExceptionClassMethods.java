//import java.lang.*;
class method{
    static void meth(){
        try{
        int a = 2;
        int b = 3-3;
        int c = a/b;
    }
    catch (Exception e){
        e.printStackTrace();
    }
    }
}
public class ExceptionClassMethods {
    public static void main(String args[])throws Exception{
        method.meth();
    }
}
