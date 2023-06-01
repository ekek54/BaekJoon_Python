import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] board;
    public static void main(String[] args) throws IOException{
        init();
        long[][] upward = bfs(N - 1, 0, new int[] {-1, 0}, new int[] {0, 1});
        long[][] downward = bfs(N - 1, M - 1, new int[] {-1, 0}, new int[] {0, -1});
        //pb(upward);
        //System.out.println(" ");
        //pb(downward);
        //System.out.println(" ");
        System.out.println(calcScore(upward, downward));
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    static long[][] bfs(int srcR, int srcC, int[] dr, int[] dc) {
        long[][] result = new long[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                result[i][j] = Long.MIN_VALUE;
            }
        }
        boolean[][] visit = new boolean[N][M];
        Queue<int[]> que = new LinkedList<>();
        result[srcR][srcC] = board[srcR][srcC];
        visit[srcR][srcC] = true;
        que.add(new int[] {srcR, srcC});
        while (!que.isEmpty()) {
            int[] cur = que.poll();
            int curR = cur[0];
            int curC = cur[1];
            for (int i = 0; i < 2; i++) {
                int nxtR = curR + dr[i];
                int nxtC = curC + dc[i];
                if (outOfBound(nxtR, nxtC)) continue;
                result[nxtR][nxtC] = Math.max(result[nxtR][nxtC], result[curR][curC] + board[nxtR][nxtC]);
                if (visit[nxtR][nxtC]) continue;
                visit[nxtR][nxtC] = true;
                que.add(new int[] {nxtR, nxtC});
            }
        }
        return result;
    }

    static boolean outOfBound(int r, int c){
        return r < 0 || N <= 0 || c < 0 || M <= c;
    }

    static void pb(long[][] board){
        for (int i = 0; i < board.length; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }

    static long calcScore(long[][] upward, long[][] downward) {
        long result = Long.MIN_VALUE;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                result = Math.max(result, upward[i][j] + downward[i][j]);
            }
        }
        return result;
    }
}
