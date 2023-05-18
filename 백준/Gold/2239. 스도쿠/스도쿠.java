import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[][] board = new int[9][9];
    static int N = 9;

    public static void main(String[] args) {
        init();
        dfs(0);
        pb(board);
    }

    static void init() {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < N; i++) {
            String numStr = sc.nextLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(numStr.substring(j, j + 1));
            }
        }
    }

    static void pb(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            String rowStr = "";
            for(int j = 0; j < 9; j++){
                rowStr += board[i][j];
            }
            System.out.println(rowStr);
        }
    }

    static boolean dfs(int cnt) {
        if (cnt == 81) {
            return true;
        }
        int r = cnt / 9;
        int c = cnt % 9;
        if (board[r][c] != 0) {
            if (dfs(cnt + 1)) return true;
        } else {
            for (int i = 1; i <= 9; i++) {
                if (isPossible(i, r, c)) {
                    board[r][c] = i;
                    if (dfs(cnt + 1)) return true;
                    board[r][c] = 0;
                }
            }
        }
        return false;
    }

    static boolean isPossible(int n, int r, int c) {
        return !isInRow(n, r) && !isInCol(n, c) && !isInBox(n, r, c);
    }

    static boolean isInRow(int n, int r) {
        for (int i = 0; i < 9; i++) {
            if (board[r][i] == n) return true;
        }
        return false;
    }

    static boolean isInCol(int n, int c) {
        for (int i = 0; i < 9; i++) {
            if (board[i][c] == n) return true;
        }
        return false;
    }

    static boolean isInBox(int n, int r, int c) {
        int boxStartR = (r / 3) * 3;
        int boxStartC = (c / 3) * 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++){
                if (board[boxStartR + i][boxStartC + j] == n) return true;
            }
        }
        return false;
    }
}
