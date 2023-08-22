import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static int[] satisfaction;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        init();
        int[] overSatisfaction = new int[N];
        int[] startFrom = new int[N];
        Arrays.fill(overSatisfaction, -1);
        Arrays.fill(startFrom, -1);
        calcOverSatisfaction(overSatisfaction, startFrom);
        bottomUp(overSatisfaction, startFrom);
        System.out.println(dp[N]);
    }

    private static void bottomUp(int[] overSatisfaction, int[] startFrom) {
        dp[0] = overSatisfaction[0] == -1 ? 0 : overSatisfaction[0];

        for (int i = 0; i < N; i++) {
            if (overSatisfaction[i] == -1) dp[i + 1] = dp[i];
            else dp[i + 1] = Math.max(dp[i] , dp[startFrom[i]] + overSatisfaction[i]);
        }
    }

    private static void calcOverSatisfaction(int[] overSatisfaction, int[] startFrom) {
        int l = 0;
        int r = 0;
        int sum = 0;
        while (l <= r && r < N) {
            if (sum < K) {
                r++;
                sum += satisfaction[r - 1];
                if (sum >= K) {
                    overSatisfaction[r - 1] = sum - K;
                    startFrom[r - 1] = l;
                }
            } else {
                sum -= satisfaction[l];
                l++;
            }
        }
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        satisfaction = new int[N];
        dp = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            satisfaction[i] = Integer.parseInt(st.nextToken());
        }
    }
}
