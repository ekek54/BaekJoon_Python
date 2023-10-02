import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static String[] board;
    static Dist[][] dists;
    static int startR, startC;
    static int flowerR, flowerC;
    static int[] dr = new int[]{1, -1, 0, 0};
    static int[] dc = new int[]{0, 0, 1, -1};


    public static void main(String[] args) throws IOException {
        initBoard();
        initStartRC();
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.dist.compareTo(o2.dist));
        Node startNode = new Node(new Dist(0, 0), startR, startC);
        pq.add(startNode);
        while (!pq.isEmpty()) {
            Node curNode = pq.poll();
            if (curNode.dist.compareTo(dists[curNode.r][curNode.c]) < 0) continue;
            for (int i = 0; i < 4; i++) {
                int nr = curNode.r + dr[i];
                int nc = curNode.c + dc[i];
                if (isOutOfBound(nr, nc)) continue;
                Dist nxtDist = new Dist(curNode.dist.onTheG, curNode.dist.nxtTheG);
                if (isOnTheGarbage(nr, nc)) {
                    nxtDist.onTheG++;
                } else if (!(board[nr].charAt(nc) == 'F') && isNxtToTheGarbage(nr, nc)) {
                    nxtDist.nxtTheG++;
                }
                if (dists[nr][nc].compareTo(nxtDist) > 0) {
                    pq.add(new Node(nxtDist, nr, nc));
                    dists[nr][nc] = nxtDist;
                }
            }
        }
//        System.out.println(Arrays.deepToString(dists));
        System.out.println(dists[flowerR][flowerC]);
    }

    private static boolean isOnTheGarbage(int r, int c) {
        return board[r].charAt(c) == 'g';
    }

    private static boolean isNxtToTheGarbage(int r, int c) {
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (isOutOfBound(nr, nc)) continue;
            if (isOnTheGarbage(nr, nc)) return true;
        }
        return false;
    }

    private static boolean isOutOfBound(int nr, int nc) {
        return nr < 0 || N <= nr || nc < 0 || M <= nc;
    }

    private static void initStartRC() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i].charAt(j) == 'S') {
                    startR = i;
                    startC = j;
                }
                if (board[i].charAt(j) == 'F') {
                    flowerR = i;
                    flowerC = j;
                }
            }
        }
        dists[startR][startC] = new Dist(0, 0);
    }

    private static void initBoard() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new String[N];
        for (int i = 0; i < N; i++) {
            board[i] = br.readLine();
        }
        dists = new Dist[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                dists[i][j] = new Dist(Integer.MAX_VALUE, Integer.MAX_VALUE);
            }
        }
    }

    private static class Dist implements Comparable {
        public int onTheG;
        public int nxtTheG;

        public Dist(int onTheG, int nxtTheG) {
            this.onTheG = onTheG;
            this.nxtTheG = nxtTheG;
        }

        @Override
        public int compareTo(Object o) {
            if (!(o instanceof Dist)) throw new IllegalStateException();
            Dist d = (Dist) o;
            if (this.onTheG == d.onTheG) return this.nxtTheG - d.nxtTheG;
            return this.onTheG - d.onTheG;
        }

        @Override
        public String toString() {
            return onTheG + " " + nxtTheG;
        }
    }

    private static class Node {
        public Dist dist;
        public int r;
        public int c;

        public Node(Dist dist, int r, int c) {
            this.dist = dist;
            this.r = r;
            this.c = c;
        }
    }
}
