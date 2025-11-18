//In java, the primitive datatypes are pass-by-value and the objects are pass-by-reference
public class ArgumentPassing {
    public static void main(String[] args) {
        int primitive = 1;
        MyObj obj = new MyObj();
        forPrimitive(primitive);
        forObject(obj);
        System.out.println("after the function call, primitive:" + primitive);
        System.out.println("after the function call, x of MyObj:" + obj.x);
    }
    static void forPrimitive(int a){
        a = 99;
    }
    static void forObject(MyObj mo){
        mo.x = 99;
    }
}
class MyObj{
    int x = 1;
}
