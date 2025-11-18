import java.util.*;
class ValidParanthesis {
    public boolean isValid(String s) {
        char[] chars = s.toCharArray();
        HashMap<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        Stack<Character> stack = new Stack<>();
        //if (map.containsKey(stack[0])) stack.push()
        //System.out.println(map.containsKey('('));
        for (char i : chars){
            System.out.println(i);
            if (map.containsKey(i)){
                System.out.println("first works");
                stack.push(i);
            }
            else{
                if(map.containsValue(i)){
                    
                    if (stack.isEmpty()) return false;
                    System.out.println("first works");
                    if (map.get(stack.pop()) != i) return false;
                }
            }
        }
        if (! stack.isEmpty()) return false;
        else return true;

    }
}