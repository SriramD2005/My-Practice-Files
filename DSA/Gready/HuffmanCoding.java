import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Comparator;
public class HuffmanCoding {
    public static void main(String args[]){
        HuffmanCoding hc = new HuffmanCoding();
        Node root = hc.constructTree();
        hc.codeIt(root);
    }
    Node constructTree(){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        Node nodes[] = new Node[n];
        String line;
        Comparator<Node> comparator = (a, b) -> a.freq - b.freq;
        PriorityQueue<Node> pq = new PriorityQueue<>(comparator);
        for (int i = 0; i < n; i++){
            line = sc.nextLine();
            String chfq[] = line.split(" ");
            nodes[i] = new Node();
            nodes[i].c = chfq[0].charAt(0);
            nodes[i].freq = Integer.parseInt(chfq[1]);
            pq.add(nodes[i]);    
        }
        Node left = new Node(), right, joint;
        while (! pq.isEmpty()){
            left = pq.poll();
            if (! pq.isEmpty()) right = pq.poll();
            else break;
            joint = new Node(left.freq + right.freq, left, right);
            pq.add(joint);
        }
        return left; // the root node
    }
    void codeIt(Node root){
        //Using pre-order traversal
        String code = new String();
        preOrder(root, code);
    }
    void preOrder(Node root, String code){
        if (! (root == null)){
            preOrder(root.left, code+"0");
            if (root.c != 0){
                System.out.println("code of " + root.c +" is " + code);
            }
            preOrder(root.right, code+"1");
        }
    }
    
}
class Node{
    char c;
    int freq;
    Node left, right;
    Node(int freq, Node left, Node right){
        this.c = 0;
        this.freq = freq;
        this.left = left;
        this.right = right;
    }
    Node(){
        c = 0;
        freq = 0;
        left = null;
        right = null;
    }
}