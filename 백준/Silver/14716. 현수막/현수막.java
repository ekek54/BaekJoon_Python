import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] board;
    static boolean[][] visit;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        init();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visit[i][j]) continue;
                if (board[i][j] == 1) {
                    floodFill(i, j);
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        visit = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    private static void floodFill(int srcR, int srcC) {
        int[] dr = new int[]{-1, -1, -1, 1, 1, 1, 0, 0};
        int[] dc = new int[]{-1, 0, 1, -1, 0, 1, 1, -1};
        Queue<RC> que = new LinkedList<>();
        que.add(new RC(srcR, srcC));
        visit[srcR][srcC] = true;
        while (!que.isEmpty()) {
            RC curRC = que.poll();
            for (int i = 0; i < 8; i++) {
                int nr = curRC.r + dr[i];
                int nc = curRC.c + dc[i];
                if (oob(nr, nc)) continue;
                if (visit[nr][nc]) continue;
                if (board[nr][nc] == 0) continue;
                visit[nr][nc] = true;
                que.add(new RC(nr, nc));
            }
        }
    }

    private static boolean oob(int nr, int nc) {
        return nr < 0 || N <= nr || nc < 0 || M <= nc;
    }

    static class RC{
        public int r;
        public int c;

        public RC(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}
