public class object_wrapper {
    public static void main(String args[]){
        int x=2;
        Integer y=x;
        System.out.println(y.getClass().getName());/*the Integer is the object wrapper for the primitive int
the HashMap is refenced to <Integer,anytype> because the reference typecast or wraps the primitive int to an object*/
    }
}
