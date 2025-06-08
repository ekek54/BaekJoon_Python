import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N, M;

    public static void main(String[] args) throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[][] board = new int[N][M];
        int[][] dist = new int[N][M];

        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(String.valueOf(input.charAt(j)));
            }

        }

        Queue<int[]> que = new LinkedList<>();

        que.add(new int[] {0, 0});
        board[0][0] = 0;
        dist[0][0] = 1;

        int[] dr = new int[] {1, -1, 0, 0};
        int[] dc = new int[] {0, 0, 1, -1};

        while (!que.isEmpty()) {
            int[] cur = que.poll();

            for (int i = 0; i < 4; i++) {
                int nr = cur[0] + dr[i];
                int nc = cur[1] + dc[i];
                if (oob(nr, nc)) continue;
                if (board[nr][nc] == 0) continue;
                board[nr][nc] = 0;
                que.add(new int[] {nr, nc});
                dist[nr][nc] = dist[cur[0]][cur[1]] + 1;
            }
        }

        System.out.println(dist[N - 1][M - 1]);
    }

    private static boolean oob(int r, int c) {
        return r < 0 || N <= r || c < 0 || M <= c;
    }
}
