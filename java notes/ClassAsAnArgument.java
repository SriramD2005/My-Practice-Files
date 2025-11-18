public class ClassAsAnArgument {
    public static <T> String getsClass(Class<? extends TheClass<T>> clazz) throws Exception {
        TheClass<T> x = clazz.getDeclaredConstructor(String.class).newInstance("hello");
        x.printit(); // optional print
        return x.str.toString(); // safe, T is String here
    }

    public static void main(String[] args) throws Exception {
        ClassAsAnArgument ca = new ClassAsAnArgument();
        String result = ca.getsClass(TheClass.class); // works now!
        System.out.println("Returned: " + result);
    }
}