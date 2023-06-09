import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
    static private final int INF = Integer.MAX_VALUE;
    static int W, H;
    static char[][] board;
    static int desR, desC;

    public static void main(String[] args) throws IOException {
        init();
        //pb();
        System.out.println(dijk());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        board = new char[H][W];
        for (int i = 0; i < H; i++) {
            board[i] = br.readLine().toCharArray();
        }
    }

    static void pb() {
        for (char[] row : board) {
            System.out.println(Arrays.toString(row));
        }
    }

    static void pb(int[][] board) {
        for (int[] row : board) {
            System.out.println(Arrays.toString(row));
        }
    }

    static int dijk() {
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        PriorityQueue<State> pq = new PriorityQueue<>();
        int[][][] dist = new int[H][W][4];
        initDist(dist);
        addStartState(pq, dist);
        initDestination();
        while (!pq.isEmpty()) {
            State curState = pq.poll();
            //System.out.println(curState);
            if (dist[curState.r][curState.c][curState.direction] < curState.mirrorCount) continue;
            for (int i = 0; i < 4; i++) {
                int nr = curState.r + dr[i];
                int nc = curState.c + dc[i];
                if (outOfBound(nr, nc)) continue;
                if (board[nr][nc] == '*') continue;
                if (isOpposite(i, curState.direction)) continue;
                int nxtMirrorCount = i == curState.direction ? curState.mirrorCount : curState.mirrorCount + 1;
                if (nxtMirrorCount < dist[nr][nc][i]) {
                    State nxtState = new State(nr, nc, i, nxtMirrorCount);
                    dist[nr][nc][i] = nxtMirrorCount;
                    pq.add(nxtState);
                }
            }
        }
        //pb(dist);
        return Arrays.stream(dist[desR][desC]).min().getAsInt();
    }

    private static void initDestination() {
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (board[i][j] == 'C') {
                    desR = i;
                    desC = j;
                }
            }
        }
    }

    private static void addStartState(PriorityQueue<State> pq, int[][][] dist) {
        boolean flag = false;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (board[i][j] == 'C') {
                    for (int k = 0; k < 4; k++) {
                        State startState = new State(i, j, k, 0);
                        dist[i][j][k] = 0;
                        pq.add(startState);
                    }
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }
    }

    private static void initDist(int[][][] dist) {
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                for (int k = 0; k < 4; k++) {
                    dist[i][j][k] = INF;
                }
            }
        }
    }

    static boolean outOfBound(int r, int c) {
        return r < 0 || H <= r || c < 0 || W <= c;
    }

    static boolean isOpposite(int dir1, int dir2) {
        if (dir1 == 0 && dir2 == 1) {
            return true;
        }
        if (dir1 == 1 && dir2 == 0) {
            return true;
        }
        if (dir1 == 2 && dir2 == 3) {
            return true;
        }
        return dir1 == 3 && dir2 == 2;
    }

    static class State implements Comparable {
        private final int r;
        private final int c;
        private final int direction;
        private final int mirrorCount;

        public State(int r, int c, int direction, int mirrorCount) {
            this.r = r;
            this.c = c;
            this.direction = direction;
            this.mirrorCount = mirrorCount;
        }

        @Override
        public int compareTo(Object o) {
            if (o instanceof State) {
                State s = (State) o;
                return mirrorCount - s.mirrorCount;
            }
            return 0;
        }

        @Override
        public String toString() {
            return "State{" +
                    "r=" + r +
                    ", c=" + c +
                    ", direction=" + direction +
                    ", mirrorCount=" + mirrorCount +
                    '}';
        }
    }
}
