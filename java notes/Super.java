class SuperClass{
    int sMember;
    SuperClass(int x){
        sMember = x; 
    }
    void sPrinter(){
        System.out.println("Printing..."+sMember);
    }
}
class SubClass extends SuperClass{
    SubClass(int y){
        super(y);
    }
    void subPrinter(){
        super.sPrinter();
    }
    
}
public class Super{
    public static void main(String args[]){
    SubClass s = new SubClass(55);
    s.subPrinter();
}
}