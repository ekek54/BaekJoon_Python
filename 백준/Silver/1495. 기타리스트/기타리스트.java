import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static int N, S, M;
    public static int[] V;
    public static int[][] dp;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(bottomUp());
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            V[i] = Integer.parseInt(st.nextToken());
        }
        dp = new int[N + 1][M + 1];
        dp[0][S] = 1;
    }

    public static int bottomUp() {
        int result = -1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= M; j++) {
                if (dp[i][j] == 0) continue;
                if (j + V[i] <= M) dp[i + 1][j + V[i]] = 1;
                if (0 <= j - V[i]) dp[i + 1][j - V[i]] = 1;
            }
        }

        for (int i = 0; i <= M; i++) {
            if (dp[N][i] == 1){
                result = Math.max(result, i);
            }
        }
        return result;
    }
}
