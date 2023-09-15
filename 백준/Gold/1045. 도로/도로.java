import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<Edge> edgeList = new ArrayList<>();
    static int N, M;
    static String[] board;
    static int[] parent;
    static int[] endPointCnt;

    public static void main(String[] args) throws IOException {
        init();

        //정렬된 엣지 리스트 만들기
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (board[i].charAt(j) == 'Y') {
                    Edge edge = new Edge(i, j);
                    edgeList.add(edge);
                }
            }
        }
        edgeList.sort(((o1, o2) -> {
            if (o1.A == o2.A) {
                return o1.B - o2.B;
            }
            return o1.A - o2.A;
        }));

        //MST 만들기
        int notNeccesary = M - (N - 1);

        for (Edge edge : edgeList) {
            if (union(edge.A, edge.B)) {
                endPointCnt[edge.A]++;
                endPointCnt[edge.B]++;
            }else if(notNeccesary > 0){
                endPointCnt[edge.A]++;
                endPointCnt[edge.B]++;
                notNeccesary--;
            }
        }

        if (isMST() && notNeccesary == 0) {
            StringBuilder sb = new StringBuilder();
            for (int cnt : endPointCnt) {
                sb.append(cnt).append(" ");
            }
            System.out.println(sb);
//            System.out.println(Arrays.toString(parent));
        }else System.out.println(-1);
    }

    private static boolean isMST() {
        for (int i = 0; i < N; i++) {
            if (find(i) != 0) return false;
        }
        return true;
    }

    private static int find(int a) {
        if (a == parent[a]) return a;
        parent[a] = find(parent[a]);
        return parent[a];
    }

    private static boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a < b) {
            parent[b] = a;
            return true;
        } else if (a > b) {
            parent[a] = b;
            return true;
        } else return false;
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new String[N];
        parent = new int[N];
        endPointCnt = new int[N];
        for (int i = 0; i < N; i++) {
            board[i] = br.readLine();
            parent[i] = i;
        }
    }

    static class Edge {
        public int A;
        public int B;

        public Edge(int A, int B) {
            this.A = A;
            this.B = B;
        }
    }
}
