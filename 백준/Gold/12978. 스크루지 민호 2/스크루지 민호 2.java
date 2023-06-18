import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();

    static int[][] dp;
    private static boolean[] visit;

    public static void main(String[] args) throws IOException {
        init();
        bottomUp();
        System.out.println(Math.min(dp[0][0], dp[0][1]));
//        System.out.println("dp = " + Arrays.deepToString(dp));
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            adjList.add(new ArrayList<>());
        }
        dp = new int[N][2];
        visit = new boolean[N];
        for (int[] ints : dp) {
            ints[1] = 1;
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;
            adjList.get(u).add(v);
            adjList.get(v).add(u);
        }
    }

    public static void bottomUp() {
        visit[0] = true;
        dfs(0);
    }
    public static void dfs(int node) {
        for (Integer adj: adjList.get(node)) {
            if (visit[adj]) continue;
            visit[adj] = true;
            dfs(adj);
            dp[node][0] += dp[adj][1];
            dp[node][1] += Math.min(dp[adj][0], dp[adj][1]);
        }
    }
}
