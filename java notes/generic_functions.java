public class generic_functions<a,b> {
    public static void main(String args[]){
        ex<Integer,Integer> x = new ex<>(2,3);
        System.out.println(x.x+" "+x.y);
    }
}
class ex<a,b>{
    a x;
    b y;
    ex(a x, b y){
        this.x = x;
        this.y = y;
    }
    a returner(a x){
        a t = x;
        return t;
    }
}