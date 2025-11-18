import java.util.HashMap;
public class HashCodeMethod {
    public static void main(String args[]){
        HashMap<MyObjs, Integer> hm = new HashMap<>();
        hm.put(new MyObjs(4,5), 5);
        hm.put(new MyObjs(5, 4), 7);//collision
        System.out.println(hm.get(new MyObjs(4,5)));
        Integer a = 5;
        Integer b = 6;
        System.out.println(a == b);
    }
}
class MyObjs{
    int mem1;
    int mem2;
    MyObjs(int in, int str){
        mem1 = in;
        mem2 = str;
    }
    @Override
    public boolean equals(Object o){
        //return this == o;
        MyObjs mo = (MyObjs) o;
        System.out.println("my custom equals");
        return this.mem1 == mo.mem1 && this.mem2 == mo.mem2;
    }
    @Override
    public int hashCode(){
        return (mem1 + mem2) % 10;
    }

}