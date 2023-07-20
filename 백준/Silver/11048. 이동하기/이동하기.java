import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int N, M;
    public static int[][] board;
    public static int[][] dp;
    public static int[] dr = {1, 0, 1};
    public static int[] dc = {0, 1, 1};


    public static void main(String[] args) throws IOException {
        init();
        System.out.println(dijk());
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        dp = new int[N + 1][M + 1];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    public static int dijk() {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                List<Integer> candid = new ArrayList<>();
                for (int k = 0; k < 3; k++) {
                    candid.add(dp[i - dr[k]][j - dc[k]]);
                }
                dp[i][j] = candid.stream().max(Integer::compareTo).orElse(0) + board[i - 1][j - 1];
            }
        }
//        System.out.println(Arrays.deepToString(dp));
        return dp[N][M];
    }

}
