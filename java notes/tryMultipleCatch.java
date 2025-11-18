public class tryMultipleCatch {
    public static void main(String args[]){
        try{
            int i = args.length;
            System.out.println(3/i);
            System.out.println(args[2]);
        }
        catch (ArithmeticException e){
            System.out.println("the Zero division error");
        }
        catch (IndexOutOfBoundsException e){
            System.out.println("the index is out of bound of the array");
        }
        finally{
            System.out.println(" the finally block always executes");
        }

    }


}
