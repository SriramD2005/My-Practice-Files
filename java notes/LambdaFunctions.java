/*Lambda functions are used to directly instantiate a
funcitonal interface(interface with only one abstract method)
directly*/
//in lambda the this points the object of the outer class
//but in inner class(nested), the this points the inner object no the outer
// to poin the object of the outer class you gotta give: "kOuterClassName.this"
public class LambdaFunctions{
    int x = -99;
    public static void main(String args[]){
        //instantiation using lambda function
        FunctionalInterface fi = (x) -> x*x;
        System.out.println(fi.square(5));
    }
    void thisDemo(){
        FunctionalInterface fi = (x) -> {
            System.out.println(this.x);
            System.out.println("in lambda the this points the object of the outer class");
            return x*x;
        };
    }
}
interface FunctionalInterface{
    
    int square(int x);
}
interface FunctionalInterface2{
    int mult(int x, int y);
}