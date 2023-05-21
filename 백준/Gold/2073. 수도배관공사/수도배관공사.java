import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int MAX_CAPACITY = (int) 2e32;
    static int D, P;
    static int[] L, C;

    static int[][] dp;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(topDown(D, P - 1));
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        D = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        L = new int[P];
        C = new int[P];
        dp = new int[D + 1][P];

        for (int i = 0; i <= D; i++) {
            for (int j = 0; j < P; j++) {
                dp[i][j] = -1;
            }
        }
        for (int i = 0; i < P; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            L[i] = l;
            C[i] = c;
        }
    }

    static int topDown(int i, int j) {
        if (i == 0) return MAX_CAPACITY;
        if (j < 0) return 0;
        if (dp[i][j] != -1) return dp[i][j];
        int result = 0;
        if (j - 1 >= 0) {
            result = topDown(i, j - 1);
        }
        if (i - L[j] >= 0) {
            result = Math.max(result, Math.min(topDown(i - L[j], j - 1), C[j]));
        }
        dp[i][j] = result;
        return result;
    }
}
