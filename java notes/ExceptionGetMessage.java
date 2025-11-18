public class ExceptionGetMessage {
    public static void main(String args[]){
        int x = 2;
        try{
            throw new MyException("the message");
        }
        catch(MyException e){
            System.out.println(e.getMessage());
        }
    }
}
class MyException extends Exception{
    MyException(String msg){
        super(msg);
    }

}
