import java.io.*;
import java.util.*;

public class Main {
    public static int N, M, H;
    public static List<List<Integer>> students = new ArrayList<>();
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        
        for (int i = 0; i < N; i++) {
            List<Integer> student = new ArrayList<>();
            student.add(0);
            students.add(student);
            StringTokenizer topsST = new StringTokenizer(br.readLine());
            while (topsST.hasMoreTokens()) {
                student.add(Integer.parseInt(topsST.nextToken()));
            }
        }

        int[][] dp = new int[N + 1][H + 1];
        
        Arrays.fill(dp[0], -1);
        
        dp[0][0] = 1;
        for (int i = 1; i <= N; i++) {
            List<Integer> tops = students.get(i - 1);
            for (int j = 0; j <= H; j++) {
                for (Integer top: tops) {
                    if (j - top >= 0 && dp[i - 1][j - top] != -1) {
                        dp[i][j] += dp[i - 1][j - top];
                        dp[i][j] %= 10007;
                    }
                }
            }
        }

        System.out.println(dp[N][H]);
    }
}
