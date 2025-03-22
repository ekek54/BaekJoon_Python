import java.util.*;

class Solution {
    public int solution(int[][] info, int n, int m) {
        int answer = 0;
        int[][] dp = new int[info.length][m];
        for (int i = 0; i < info.length; i++) {
            for (int j = 0; j < m; j++) {
                dp[i][j] = n;
            }
        }
        if (info[0][1] < m) {
            dp[0][info[0][1]] = 0;
        }
        dp[0][0] = info[0][0];
        for (int i = 1; i < info.length; i++) {
            for (int j = 0; j < m; j++) {
                if (dp[i - 1][j] != n) {
                    if (dp[i - 1][j] + info[i][0] < n) {
                        dp[i][j] = dp[i - 1][j] + info[i][0];
                    }
                }
                if (j - info[i][1] >= 0 && dp[i - 1][j - info[i][1]] != n) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][j - info[i][1]]);
                }
            }
        }
        // pb(dp);
        answer = n;
        for (int i = 0; i < m; i++) {
            answer = Math.min(dp[info.length - 1][i], answer);
        }
        if (answer == n) {
            answer = -1;
        }
        return answer;
    }
    
    private void pb(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }
}