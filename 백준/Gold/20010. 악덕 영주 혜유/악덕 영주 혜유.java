import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static int N, K;
    public static ArrayList<Edge> edgeList = new ArrayList<>();
    public static int[] parent;
    public static ArrayList<ArrayList<int[]>> adjList = new ArrayList<>();
    static class Edge{
        public final int nodeA;
        public final int nodeB;
        public final int cost;

        public Edge(int nodeA, int nodeB, int cost) {
            this.nodeA = nodeA;
            this.nodeB = nodeB;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(MST());
        System.out.println(calcLongestLength());
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            Edge edge = new Edge(A, B, cost);
            edgeList.add(edge);
        }
    }

    public static int find(int a){
        if (parent[a] == a) {
            return a;
        }else{
            parent[a] = find(parent[a]);
            return parent[a];
        }
    }

    public static boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a < b) {
            parent[b] = a;
        } else if (a > b) {
            parent[a] = b;
        } else return false;
        return true;
    }

    public static int MST() {
        int result = 0;
        edgeList.sort((o1, o2) -> o1.cost - o2.cost);
        for (Edge edge : edgeList) {
            if (union(edge.nodeA, edge.nodeB)){
                result += edge.cost;
                adjList.get(edge.nodeA).add(new int[] {edge.nodeB, edge.cost});
                adjList.get(edge.nodeB).add(new int[] {edge.nodeA, edge.cost});
            }
        }
        return result;
    }

    public static int calcLongestLength(){
        boolean[] visit = new boolean[N];
        int endNodeOfDiameter = dfs(0, 0, visit).node;
        visit = new boolean[N];
        return dfs(endNodeOfDiameter,0, visit).dist;
    }

    private static State dfs(int node, int dist, boolean[] visit){
        visit[node] = true;
        State curState = new State(node, dist);
        for (int[] nxt : adjList.get(node)) {
            int nxtNode = nxt[0];
            int cost = nxt[1];
            if (visit[nxtNode]) continue;
            State nxtState = dfs(nxtNode, dist + cost, visit);
            if (curState.dist < nxtState.dist) {
                curState = nxtState;
            }
        }
        return curState;
    }

    static class State{
        public int node;
        public int dist;

        public State(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }

}

