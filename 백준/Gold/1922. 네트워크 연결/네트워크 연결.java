import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static class Edge {
        public int A, B;
        public int weight;

        public Edge(int A, int B, int weight) {
            this.A = A;
            this.B = B;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return A + "-" + B + ":" + weight;
        }
    }

    static int N, M;
    static ArrayList<Edge> edgeList = new ArrayList<>();
    static int[] parent;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(prim());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        StringTokenizer st;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());
            edgeList.add(new Edge(a, b, c));
        }
        edgeList.sort((e1, e2) -> {
            return e1.weight - e2.weight;
        });
    }

    static int find(int a) {
        if (parent[a] == a) return a;
        parent[a] = find(parent[a]);
        return parent[a];
    }
    static boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a < b) {
            parent[b] = a;
            return true;
        }else if(a > b) {
            parent[a] = b;
            return true;
        }else {
            return false;
        }
    }

    static int prim() {
        int result = 0;
        for(Edge edge: edgeList) {
            if (union(edge.A, edge.B)) {
                result += edge.weight;
            }
        }
        return result;
    }
}
