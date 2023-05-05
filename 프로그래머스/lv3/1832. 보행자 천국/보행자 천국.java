import java.util.*;
class Solution {
    int MOD = 20170805;
    int[][][] dp;
    int[][] board;
    public int solution(int m, int n, int[][] cityMap) {
        board = cityMap;
        dp = new int[m][n][2];
        for (int i = 0; i < m; i ++){
            for(int j = 0; j < n; j ++){
                dp[i][j][0] = -1;
                dp[i][j][1] = -1;
            }
        }
        int answer = topDown(m - 1, n - 1, 0) + topDown(m - 1, n - 1, 1);
        return answer % MOD;
    }
    public int topDown(int r, int c, int d){
        if (r < 0 || c < 0) return 0;
        if (board[r][c] == 1) return 0;
        if (dp[r][c][d] != -1) return dp[r][c][d];
        if (r == 0 && c == 0) return 1;
        int ret = 0;
        if (d == 0 && c >= 1){
            ret += topDown(r, c - 1, 0);
            if (board[r][c - 1] == 0 && !(r == 0 && c - 1 == 0)) {
                ret += topDown(r, c - 1, 1);
            }
        }
        else if(d == 1 && r >= 1){
            ret += topDown(r - 1, c, 1);
            if (board[r - 1][c] == 0 && !(r - 1 == 0 && c == 0)) {
                ret += topDown(r - 1, c, 0);
            }
        }
        dp[r][c][d] = ret % MOD;
        return dp[r][c][d];
    }
}