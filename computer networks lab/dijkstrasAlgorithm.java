//incomplete
import java.util.*;
public class dijkstrasAlgorithm {
    static class Edge{
        int target;
        int weight;
        Edge(int target, int weight){
            this.target = target;
            this.weight= weight;
        }
    }
    static class Node implements comparable{
        int id;
        int distance;
        Node(int id, int distance){
            this.id = id;
            this.distance = distance;
        }
        public int compareTo(Node other){
            return this.distance - other.distance;
        }
    }
    static void dijkstra(List<List<Edge>> graph, int start){
        PriorityQueue<Node> minheap = new PriorityQueue<>();
        Node sNode = new Node(start, 0);
        int[] dist = new int[graph.size()];
        minheap.offer(sNode);
        dist[start] = 0;
        Node curr;
        while (!minheap.isEmpty()){
            curr = minheap.poll();
            for(Edge e : graph.get(curr.id)){
                Node newNode = new (Edge.target,dist[curr.id]+)
            }
        }
    }
    public static void main(String args[]){
        
    }
}
