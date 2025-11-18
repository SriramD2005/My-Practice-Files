//by using ananymous class, you dont have to create a class with a name that implements the interface or extends a class
public class AnanymousClass {
    static Animal dog = new Animal() {
        public void sound(){
            System.out.println("ruf ruf");
        }
    };
    public static void main(String args[]){
        dog.sound();
    };
}
interface Animal{
    void sound();
}