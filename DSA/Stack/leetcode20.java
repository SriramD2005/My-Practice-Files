/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.*;
class leetcode20 {
    public boolean isPalindrome(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        if (slow.next == null) return true;
        boolean iseven = true;
        Stack<ListNode> s = new Stack<>();
        while (fast != null){
            s.push(slow);
            slow = slow.next;
            if (fast.next != null) {fast = fast.next.next;}
            else{
                System.out.println("in wrong else");
                System.out.println(fast.val);
                fast = fast.next;
                iseven = false;
            }
        }//here stack is 1 and 0
        if (!iseven) {
            ListNode ln = s.pop();
            System.out.print("poped val ");
            System.out.println(ln.val);
            System.out.println("slow");
            System.out.println(slow.val);
            //slow = slow.next;
            //System.out.println(slow.val);
        }
        Iterator<ListNode> iterator = s.iterator();
        while(iterator.hasNext()) System.out.print(iterator.next().val);
        System.out.println();
        //System.out.println(slow.val);
        while (slow != null){
            System.out.println(slow.val);
            if (slow.val != s.pop().val) return false;
            slow = slow.next;
        }
        return true;
    }
}