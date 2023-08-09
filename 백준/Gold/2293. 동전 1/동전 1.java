import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static int[] coins;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        init();
        for (int i = 1; i < N + 1; i++) {
            for (int j = 0; j < K + 1; j++) {
                int k = 0;
                while (j >= coins[i - 1] * k) {
                    dp[i][j] += dp[i - 1][j - (coins[i - 1] * k)];
                    k++;
                }
            }
        }
//        System.out.println("dp = " + Arrays.deepToString(dp));
        System.out.println(dp[N][K]);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        coins = new int[N];
        dp = new int[N + 1][K + 1];
        dp[0][0] = 1;
        for (int i = 0; i < N; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }
    }
}
