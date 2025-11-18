public class VariableArguments {
    public static void main(String args[]){
        VariableArguments v = new VariableArguments();
        v.printer("hi", "hello", "how", "are", "you");
    }
    void printer(String... items){
        for (String i : items){
            System.out.println(i);
        }
    }
}
