import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
public class DFS {
    void dfs(Map<String, String[]> graph, String curr, HashSet<String> visited){
        if (visited.contains(curr)) return;
        visited.add(curr);
        System.out.print(curr + " -> ");
        String[] neighbours = graph.get(curr);
        if (neighbours == null) return;
        for (String i : neighbours){
            dfs(graph, i, visited);
        }
    }
    public static void main(String arg[]){
        HashMap<String, String[]> graph = new HashMap<>();
        graph.put("A", new String[] {"B", "C"});
        graph.put("B", new String[] {"A", "E"});
        graph.put("C", new String[] {"A", "E", "D"});
        graph.put("D", new String[] {"C"});
        graph.put("E", new String[] {"C", "B"});

        DFS dfsObj = new DFS();
        dfsObj.dfs(graph, "A", new HashSet<>());
    }
}
