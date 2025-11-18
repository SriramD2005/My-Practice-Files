public class LinkedList {
    public static void main(String args[]){

    }
}
//Linked List that can have only one datatype
class Node<a>{
    a value;
    Node<a> next;
    Node(a value, Node<a> next){
        this.value = value;
        this.next = next;
    }
    Node(a value){
        this.value = value;
        this.next = null;
    }
}
//Linked list that can have different datatypes
class DynamicTypedNode{
    Object value;
    DynamicTypedNode next;
    DynamicTypedNode(Object value, DynamicTypedNode next){
        this.value = value;
        this.next = next;
    }
    DynamicTypedNode(Object value){
        this(value, null);
    }
}