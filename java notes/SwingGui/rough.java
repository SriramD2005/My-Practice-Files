public class rough {
    public static void main(String args[]){
        animal a = new dog();
        //a.bark() -> this will cause an error
        dog d = (dog) a; //You cannot access the 
        d.bark();
    }
}
class animal{
    void sound(){
        System.out.println("animal sound:");
    }
}
class dog extends animal{
    void bark(){
        super.sound();
        System.out.println("barking");
    }
}