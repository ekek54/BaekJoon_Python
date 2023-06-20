import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, S, D;
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
    static int[] height;
    static boolean[] visit;

    public static void main(String[] args) throws IOException {
        init();
        visit[S] = true;
        dfs(S);
//        System.out.println("height = " + Arrays.toString(height));
        System.out.println((countShouldVisit() - 1) * 2);
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken()) - 1;
        D = Integer.parseInt(st.nextToken());
        height = new int[N];
        visit = new boolean[N];
        for (int i = 0; i < N; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            adjList.get(x).add(y);
            adjList.get(y).add(x);
        }
    }

    static void dfs(int node) {
        for (Integer adjNode : adjList.get(node)) {
            if (visit[adjNode]) continue;
            visit[adjNode] = true;
            dfs(adjNode);
            height[node] = Math.max(height[node], height[adjNode] + 1);
        }
    }

    static int countShouldVisit() {
        int result = (int) Arrays.stream(height).filter(h -> h >= D).count();
        return result == 0 ? 1 : result;
    }
}
