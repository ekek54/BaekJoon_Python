import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static int superNode = 0;
    static List<List<AdjInfo>> adjList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();

        int[] distFromSuper = new int[N];
        int[] preNode = new int[N];
        initDistFromSuper(distFromSuper);
        dijk(distFromSuper, preNode);
        Set<Connection> repairConnectionSet = new HashSet<>();
        for (int i = 1; i < N; i++) {
            int cur = i;
            while (cur != superNode) {
                repairConnectionSet.add(new Connection(cur, preNode[cur]));
                cur = preNode[cur];
            }
        }
//        System.out.println("distFromSuper = " + Arrays.toString(distFromSuper));
//        System.out.println("preNode = " + Arrays.toString(preNode));
//        System.out.println("repairConnectionSet = " + repairConnectionSet);
        System.out.println(repairConnectionSet.size());
        for (Connection connection : repairConnectionSet) {
            System.out.println(connection);
        }
    }

    private static void initDistFromSuper(int[] distFromSuper) {
        Arrays.fill(distFromSuper, Integer.MAX_VALUE);
        distFromSuper[superNode] = 0;
    }

    private static void dijk(int[] distFromSuper, int[] preNode) {
        PriorityQueue<AdjInfo> pq = new PriorityQueue<>((s1, s2) -> {
            return s1.dist - s2.dist;
        });
        pq.add(new AdjInfo(superNode, 0));
        while (!pq.isEmpty()) {
            AdjInfo curAdj = pq.poll();
            int curNode = curAdj.adjNode;
            int distFromSuperToCurNode = curAdj.dist;
            if (distFromSuper[curNode] < distFromSuperToCurNode) continue;
            for (AdjInfo adjInfo : adjList.get(curNode)) {
                int nxtNode = adjInfo.adjNode;
                int distFromCurNodeToNxtNode = adjInfo.dist;
                if (distFromSuper[nxtNode] > distFromSuperToCurNode + distFromCurNodeToNxtNode) {
                    distFromSuper[nxtNode] = distFromSuperToCurNode + distFromCurNodeToNxtNode;
                    preNode[nxtNode] = curNode;
                    pq.add(new AdjInfo(nxtNode, distFromSuper[nxtNode]));
                }
            }
        }
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken()) - 1;
            int B = Integer.parseInt(st.nextToken()) - 1;
            int C = Integer.parseInt(st.nextToken());
            adjList.get(A).add(new AdjInfo(B, C));
            adjList.get(B).add(new AdjInfo(A, C));
        }
    }

    static class AdjInfo {
        public int adjNode;
        public int dist;

        public AdjInfo(int adjNode, int dist) {
            this.adjNode = adjNode;
            this.dist = dist;
        }
    }

    static class Connection {
        public int a;
        public int b;

        public Connection(int a, int b) {
            this.a = Math.min(a, b);
            this.b = Math.max(a, b);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Connection that = (Connection) o;
            return a == that.a && b == that.b;
        }

        @Override
        public int hashCode() {
            return Objects.hash(a, b);
        }

        @Override
        public String toString() {
            return (a + 1) + " " + (b + 1);
        }
    }
}
