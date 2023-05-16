import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static int A;
    static int B;
    static int[][] board; //아이템 1, 방해물 2
    static int[][] itemRCs;
    public static void main(String[] args) {
        init();
        System.out.println(calcResult());
    }

    public static void init() {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        itemRCs = new int[A][2];
        for (int i = 0; i < A + B; i++) {
            st = new StringTokenizer(sc.nextLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            if (i < A) {
                board[r][c] = 1;
                itemRCs[i] = new int[] {r, c};
            } else {
                board[r][c] = 2;
            }
        }
        Arrays.sort(itemRCs, (e1, e2) -> {
            if (e1[0] == e2[1]) {
                return e1[1] - e2[1];
            }
            return e1[0] - e2[0];
        });
    }

    public static int calcPathCnt(int[] src, int[] des) {
        int srcR = src[0];
        int srcC = src[1];
        int desR = des[0];
        int desC = des[1];
        int n = desR - srcR + 1;
        int m = desC - srcC + 1;
        int[][] dp = new int[n][m];
        dp[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[srcR + i][srcC + j] == 2) {
                    dp[i][j] = 0;
                    continue;
                }
                if (i + 1 < n) {
                    dp[i + 1][j] += dp[i][j];
                }
                if (j + 1 < m) {
                    dp[i][j + 1] += dp[i][j];
                }
            }
        }
        return dp[n - 1][m - 1];
    }

    public static int calcResult() {
        int result = 1;
        int curR = 0;
        int curC = 0;
        for(int[] itemRC: itemRCs) {
            int nxtR = itemRC[0];
            int nxtC = itemRC[1];
            result *= calcPathCnt(new int[] {curR, curC}, new int[] {nxtR, nxtC});
            curR = nxtR;
            curC = nxtC;
        }
        return result * calcPathCnt(new int[] {curR, curC}, new int[] {N - 1, M - 1});
    }
}
