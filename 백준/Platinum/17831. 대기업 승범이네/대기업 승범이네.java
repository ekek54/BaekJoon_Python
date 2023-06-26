import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N; // [2, 200,000]
    static ArrayList<ArrayList<Integer>> childList;
    static int[] abilities;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(bottomUp());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        childList = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            childList.add(new ArrayList<>());
        }
        abilities = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N; i++) {
            int parent = Integer.parseInt(st.nextToken()) - 1;
            childList.get(parent).add(i);

        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            abilities[i] = Integer.parseInt(st.nextToken());
        }
    }

    static int bottomUp() {
        int[][] result = new int[N][2];
        dfs(0, result);
        return getMax(result[0]);
    }

    static void dfs(int node, int[][] dp) {
        if (childList.get(node).size() == 0) {
            dp[node][0] = 0;
            dp[node][1] = 0;
            return;
        }

        for (Integer child : childList.get(node)) {
            dfs(child, dp);
            dp[node][0] += getMax(dp[child]);
        }
        for (Integer child : childList.get(node)) {
            int synergy = abilities[child] * abilities[node];
            dp[node][1] = Math.max(dp[node][1], dp[node][0] - getMax(dp[child]) + dp[child][0] + synergy);
        }
    }

    private static int getMax(int[] arr) {
        return Arrays.stream(arr).max().orElseThrow();
    }
}
