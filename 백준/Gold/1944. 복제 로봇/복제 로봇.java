import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Node {
        private int r, c;

        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
        public int getR(){
            return r;
        }
        public int getC(){
            return c;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node node = (Node) o;
            return r == node.getR() && c == node.getC();
        }

        @Override
        public int hashCode() {
            return Objects.hash(r, c);
        }

        @Override
        public String toString() {
            return "Node{" +
                    "r=" + r +
                    ", c=" + c +
                    '}';
        }
    }

    static class Edge implements Comparable{
        private Node desNode;
        private int length;

        public Edge(Node desNode, int length) {
            this.desNode = desNode;
            this.length = length;
        }
        public int getLength() {
            return length;
        }

        public Node getDesNode() {
            return desNode;
        }

        @Override
        public int compareTo(Object o) {
            Edge edge = (Edge) o;
            return length - edge.getLength();
        }

        @Override
        public String toString() {
            return "Edge{" +
                    "desNode=" + desNode +
                    ", length=" + length +
                    '}';
        }
    }
    static int N, M;
    static Node startNode;
    static String[] board;
    static Map<Node, Boolean> visit = new HashMap<>();

    public static void main(String[] args) throws IOException{
        init();
        int answer = prim();
        //System.out.println(visit);
        System.out.println(visit.containsValue(false) ? -1 : answer);
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new String[N];
        for (int i = 0; i < N; i++) {
            board[i] = br.readLine();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i].charAt(j) == 'S' || board[i].charAt(j) == 'K') {
                    Node node = new Node(i, j);
                    if (board[i].charAt(j) == 'S') {
                        startNode = node;
                    }
                    visit.put(node, false);
                }
            }
        }
    }

    static int prim() {
        int result = 0;
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        Edge startEdge = new Edge(startNode, 0);
        pq.add(startEdge);
        while (!pq.isEmpty()) {
            Edge curEdge = pq.poll();
            //System.out.println(curEdge);
            Node curNode = curEdge.getDesNode();
            int curLength = curEdge.getLength();
            if (visit.get(curNode)) {
                continue;
            }
            visit.put(curNode, true);
            result += curLength;
            ArrayList<Edge> nxtEdges = bfs(curNode);
            for (Edge nxtEdge: nxtEdges) {
                if (visit.get(nxtEdge.getDesNode())) continue;
                //System.out.println(nxtEdge);
                pq.add(nxtEdge);
            }
        }
        return result;
    }

    static ArrayList<Edge> bfs(Node srcNode) {
        ArrayList<Edge> result = new ArrayList<>();
        Queue<int[]> que = new LinkedList<>();
        boolean[][] visit = new boolean[N][N];
        int[][] dist = new int[N][N];
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};

        visit[srcNode.getR()][srcNode.getC()] = true;
        que.add(new int[] {srcNode.getR(), srcNode.getC()});
        while (!que.isEmpty()) {
            int[] curRC = que.poll();
            int curR = curRC[0];
            int curC = curRC[1];
            int curDist = dist[curR][curC];
            for (int i = 0; i < 4; i++) {
                int nxtR = curR + dr[i];
                int nxtC = curC + dc[i];
                if (outOfBound(nxtR, nxtC)) continue;
                if (visit[nxtR][nxtC]) continue;
                if (board[nxtR].charAt(nxtC) == '1') continue;
                visit[nxtR][nxtC] = true;
                dist[nxtR][nxtC] = curDist + 1;
                que.add(new int[] {nxtR, nxtC});
                if (board[nxtR].charAt(nxtC) == 'S' || board[nxtR].charAt(nxtC) == 'K') {
                    Node node = new Node(nxtR, nxtC);
                    Edge edge = new Edge(node, dist[nxtR][nxtC]);
                    result.add(edge);
                }
            }
        }
        return result;
    }

    static boolean outOfBound(int r, int c) {
        return r < 0 || N <= r || c < 0 || N <= c;
    }
}
