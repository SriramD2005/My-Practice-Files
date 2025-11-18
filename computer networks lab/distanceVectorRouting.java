import java.io.BufferedReader;
import java.io.InputStreamReader;
public class distanceVectorRouting {
    public static void main(String args[])throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cost[][];
        int distance[][];
        int via[][];
        System.out.print("enter no of routers:");
        int n = Integer.parseInt(br.readLine());
        System.out.println();
        cost = new int[n][n];
        distance = new int[n][n];
        via = new int[n][n];
        System.out.println("enter the cost matrix");
        int inf = 9999;
        for (int i = 0;i<n;i++){
        String line[] = br.readLine().trim().split("\\s");
        for (int j = 0;j<n;j++){
            cost[i][j] = Integer.parseInt(line[j]);
            distance[i][j] = cost[i][j];
            if (i == j || cost[i][j] == inf) via[i][j] = -1;
            else via[i][j] = j;
        }}
        //bellman algorithm
        for (int k = 0;k<n;k++){
            for (int i = 0;i<n;i++){
                for (int j = 0;j<n;j++){
                    if (distance[i][j] > distance[k][j] + distance[i][k]){
                        distance[i][j] = distance[k][j] + distance[i][k];
                        via[i][j] = via [i][k];
                    }
                }
            }
        }
        System.out.println("source"+"\t"+"destination"+"\t"+"via");
        for (int i = 0;i<n;i++){
            for (int j = 0;j<n;j++){
                System.out.println(i+"\t\t"+j+"\t\t"+via[i][j]);
            }
        }
}
}