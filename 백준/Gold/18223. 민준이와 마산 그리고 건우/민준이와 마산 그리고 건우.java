import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main{
    public static int V, E, P;
    public static ArrayList<ArrayList<Adjacent>> adjList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(solution());
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken()) - 1;
        for (int i = 0; i < V; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());
            adjList.get(a).add(new Adjacent(b, c));
            adjList.get(b).add(new Adjacent(a, c));
        }
    }

    static class Adjacent {
        public int adjNode;
        public int dist;

        public Adjacent(int adjNode, int dist) {
            this.adjNode = adjNode;
            this.dist = dist;
        }

        @Override
        public String toString() {
            return "Adjacent{" +
                    "adjNode=" + adjNode +
                    ", dist=" + dist +
                    '}';
        }
    }

    public static String solution() {
        int[] dist = new int[V];
        int[] from = new int[V];
        for (int i = 0; i < V; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        dist[0] = 0;
        PriorityQueue<Adjacent> pq = new PriorityQueue<>((o1, o2) -> {
            return o1.dist - o2.dist;
        });
        pq.add(new Adjacent(0, 0));
        while (!pq.isEmpty()) {
            Adjacent curAdj = pq.poll();
            if (dist[curAdj.adjNode] < curAdj.dist) continue;
            for (Adjacent adjacent : adjList.get(curAdj.adjNode)) {
                if (dist[adjacent.adjNode] > dist[curAdj.adjNode] + adjacent.dist) {
                    dist[adjacent.adjNode] = dist[curAdj.adjNode] + adjacent.dist;
                    from[adjacent.adjNode] = curAdj.adjNode;
                    pq.add(new Adjacent(adjacent.adjNode, dist[adjacent.adjNode]));
                } else if (dist[adjacent.adjNode] == dist[curAdj.adjNode] + adjacent.dist) {
                    if (curAdj.adjNode == P) {
                        from[adjacent.adjNode] = curAdj.adjNode;
                    }
                }
            }
        }
        return canSave(from) ? "SAVE HIM" : "GOOD BYE";
    }

    public static boolean canSave(int[] from) {
        int cur = V - 1;
        while (true) {
            if (cur == P) return true;
            if (cur == 0) return false;
            cur = from[cur];
        }
    }
}
