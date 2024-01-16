import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static int N, M;
    public static int[] D;

    public static void main(String[] args) throws IOException{
        input();
        int[][][] dp = new int[N][M + 1][2];
        for (int i = 0; i < N; i++) {
            for (int j =0; j < M + 1; j++) {
                for (int k = 0; k < 2; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }
        dp[0][0][1] = 0;
        dp[0][1][0] = D[0];
        for (int i = 1; i < N; i++) {
            for (int j = 0; j <= M; j++) {
                for (int k = 0; k < 2; k++) {
                    if (k == 0) {
                        if (j - 1 >= 0 && isVisited(dp[i - 1][j - 1][0]))
                            dp[i][j][0] = Math.max(dp[i][j][0], dp[i - 1][j - 1][0] + D[i]);
                        if (j - 1 == 0 && isVisited(dp[i - 1][j - 1][1]))
                            dp[i][j][0] = Math.max(dp[i][j][0], dp[i - 1][j - 1][1] + D[i]);
                    } else {
                        if (j == 0 && isVisited(dp[i - 1][0][1])) 
                            dp[i][j][1] = Math.max(dp[i][j][1], dp[i - 1][0][1]);
                        if (j + 1 <= M) {
                            if (isVisited(dp[i - 1][j + 1][0]))
                                dp[i][j][1] = Math.max(dp[i][j][1], dp[i - 1][j + 1][0]);
                            if (isVisited(dp[i - 1][j + 1][1]))
                                dp[i][j][1] = Math.max(dp[i][j][1], dp[i - 1][j + 1][1]);
                        }
                    }
                }
            }
        }
//        pb(dp);
        System.out.println(dp[N - 1][0][1]);
    }

    private static boolean isVisited(int a) {
        return a != -1;
    }

    private static void input() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = new int[N];
        for (int i = 0; i < N; i++) {
            D[i] = Integer.parseInt(br.readLine());
        }
    }

    private static void pb(int[][][] board) {
        for (int[][] ints : board) {
            System.out.println(Arrays.deepToString(ints));
        }
    }
}
