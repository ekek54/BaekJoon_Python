import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int excluded = 1;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[] dp = new int[N];
        dp[0] = 1;
        for (int i = 1; i < N; i++) {
            int maximum = 0;
            for (int j = 0; j < i; j++) {
                if (arr[i] < arr[j]) {
                    maximum = Math.max(maximum, dp[j]);
                }
            }
            dp[i] = maximum + 1;
            excluded = Math.max(excluded, dp[i]);
        }
        System.out.println(N - excluded);
    }
}
