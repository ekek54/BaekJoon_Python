import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static int N, M;
    static boolean[] isVIP;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        init();
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < N + 1; i++) {
            if (isVIP[i] || isVIP[i - 1]){
                dp[i] = dp[i - 1];
            }else {
                dp[i] = dp[i - 1] + dp[i - 2];
            }
        }
//        System.out.println("dp = " + Arrays.toString(dp));
        System.out.println(dp[N]);
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        dp = new int[N + 1];
        isVIP = new boolean[N + 1];
        for (int i = 0; i < M; i++) {
            int vip = Integer.parseInt(br.readLine());
            isVIP[vip] = true;
        }
    }

}
