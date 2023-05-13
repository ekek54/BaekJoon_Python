import java.util.*;

public class Main {
    static int N;
    static int M;

    public static void main(String[] args) {
        int result = 0;
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        ArrayList<Integer>[] outAdjList = new ArrayList[N];
        ArrayList<Integer>[] inAdjList = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            outAdjList[i] = new ArrayList<>();
            inAdjList[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(sc.nextLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            a -= 1;
            b -= 1;
            outAdjList[a].add(b);
            inAdjList[b].add(a);
        }
        for (int i = 0; i < N; i++) {
            if (isPossible(i, inAdjList, outAdjList)) result ++;
        }
        System.out.println(result);
    }

    public static boolean isPossible(int src, ArrayList<Integer>[] inAdjList, ArrayList<Integer>[] outAdjList) {
        boolean[] visit = new boolean[N];
        bfs(src, inAdjList, visit);
        bfs(src, outAdjList, visit);
        for (boolean v: visit) {
            if (!v) return false;
        }
        return true;
    }

    public static void bfs(int src, ArrayList<Integer>[] adjList, boolean[] visit) {
        Queue<Integer> que = new LinkedList<>();
        visit[src] = true;
        que.add(src);
        while (!que.isEmpty()) {
            int cur = que.poll();
            for(int nxt: adjList[cur]) {
                if (visit[nxt]) continue;
                visit[nxt] = true;
                que.add(nxt);
            }
        }

    }
}
