import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] board;
    static boolean[][] check;
    static boolean[][][] visit;
    // 상, 하, 좌, 우
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(bfs());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        check = new boolean[N][M];
        visit = new boolean[N][M][4];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    static int bfs() {
        Queue<int[][]> que = new LinkedList<>();
        ArrayList<int[]> aircons = srcs();
        for(int[] src: aircons) {
            int srcR = src[0];
            int srcC = src[1];
            check[srcR][srcC] = true;
            for (int i = 0; i < 4; i++) {
                que.add(new int[][] {src, new int[] {i}});
            }
        }
        while (!que.isEmpty()) {
            int[][] cur = que.poll();
            int curR = cur[0][0];
            int curC = cur[0][1];
            int curD = cur[1][0];

            int nxtD = nxtDirection(curD, board[curR][curC]);
            if (nxtD == -1) continue;
            int nxtR = curR + dr[nxtD];
            int nxtC = curC + dc[nxtD];
            if (OOB(nxtR, nxtC)) continue;
            if (visit[nxtR][nxtC][nxtD]) continue;
            visit[nxtR][nxtC][nxtD] = true;
            check[nxtR][nxtC] = true;
            que.add(new int[][]{new int[]{nxtR, nxtC}, new int[]{nxtD}});
        }
        return checkCount();
    }

    static ArrayList<int[]> srcs() {
        ArrayList<int[]> result = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 9) {
                    result.add(new int[] {i, j});
                }
            }
        }
        return result;
    }

    static int nxtDirection(int curDirection, int boardState) {
        if (boardState == 0) return curDirection;
        if ((curDirection == 0 || curDirection == 1) && boardState == 2) return -1;
        if ((curDirection == 2 || curDirection == 3) && boardState == 1) return -1;
        if (boardState == 3) {
            if (curDirection == 0) return 3;
            if (curDirection == 1) return 2;
            if (curDirection == 2) return 1;
            if (curDirection == 3) return 0;
        }
        if (boardState == 4) {
            if (curDirection == 0) return 2;
            if (curDirection == 1) return 3;
            if (curDirection == 2) return 0;
            if (curDirection == 3) return 1;
        }
        return curDirection;
    }

    static boolean OOB(int r, int c) {
        return r < 0 || N <= r || c < 0 || M <= c;
    }

    static int checkCount() {
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (check[i][j]) result++;
            }
        }
        return result;
    }
}
