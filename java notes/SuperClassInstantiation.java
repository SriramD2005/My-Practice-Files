/*Whenever you instantiate a subclass you also implicitly instantiate the super class, if the arguments to the
constructor of the subclass is different from the arguments of the superclass constructor, then you must
then the subclass constructor should call super(arguments) explicitly*/
public class SuperClassInstantiation {
    public static void main(String args[]){
        subclass sc = new subclass();
    }
}
class superclass{
    private static int x = 0;
    superclass(){//argument int y:if the arg is given you should call the super(int) in subclass constructor explicitly
        System.out.println("the super class is instantiated when we instantiate the subclass");
        x += 100;
        //System.out.println(y);
    }
}
class subclass extends superclass{
    subclass(){
        //super("the argument from the subclass to the super class");
        System.out.println("Subclass is instantiated");
    }
}