import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static List<List<Adj>> adjList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        int r1 = findFirstFarNode(getDists(0));
        int r2 = findFirstFarNode(getDists(r1));;
//        System.out.println("r1 = " + r1);
//        System.out.println("r2 = " + r2);

        int answer = Math.max(findSecondFarDist(getDists(r1)), findSecondFarDist(getDists(r2)));
        System.out.println(answer);
    }

    private static int[] getDists(int src) {
        int[] dist = new int[N];
        boolean[] visit = new boolean[N];
        visit[src] = true;
        Queue<Integer> que = new LinkedList<>();
        que.add(src);
        while (!que.isEmpty()) {
            Integer curNode = que.poll();
            for (Adj nxt : adjList.get(curNode)) {
                if (visit[nxt.node]) continue;
                visit[nxt.node] = true;
                dist[nxt.node] = dist[curNode] + nxt.dist;
                que.add(nxt.node);
            }
        }
        return dist;
    }

    private static int findFirstFarNode(int[] dists) {
        int farDist = 0;
//        System.out.println("dists = " + Arrays.toString(dists));
        int farNode = -1;
        for (int i = 0; i < dists.length; i++) {
            if (farDist < dists[i]) {
                farDist = dists[i];
                farNode = i;
            }
        }
        return farNode;
    }

    private static int findSecondFarDist(int[] dists) {
        Arrays.sort(dists);
        return dists[dists.length - 2];
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            adjList.add(new ArrayList<>());
        }
        StringTokenizer st;
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken()) - 1;
            int B = Integer.parseInt(st.nextToken()) - 1;
            int V = Integer.parseInt(st.nextToken());
            adjList.get(A).add(new Adj(B, V));
            adjList.get(B).add(new Adj(A, V));
        }
    }

    static class Adj {
        public int node;
        public int dist;

        public Adj(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }
}
