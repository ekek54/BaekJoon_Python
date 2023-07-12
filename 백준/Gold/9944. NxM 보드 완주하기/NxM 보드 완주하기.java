import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String input;
        int caseNum = 1;
        while ((input = br.readLine()) != null) {
            st = new StringTokenizer(input);
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[][] board = new int[N][M];
            for (int i = 0; i < N; i++) {
                String row = br.readLine();
                for (int j = 0; j < M; j++) {
                    board[i][j] = (row.charAt(j) == '*') ? 1 : 0;
                }
            }
            int answer = solution(N, M, board);
            answer = answer == Integer.MAX_VALUE ? -1 : answer;
            System.out.println("Case " + caseNum++ + ": " + answer);
        }
    }

    public static int solution(int N, int M, int[][] board) {
        int result = Integer.MAX_VALUE;
        boolean[][] visit = new boolean[N][M];
        int totalEmpty = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0) totalEmpty++;
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0) {
                    visit[i][j] = true;
                    result = Math.min(result, dfs(i, j, 0, board, visit, result, totalEmpty, 1));
                    visit[i][j] = false;
                }
            }
        }
        return result;
    }

    public static int dfs(int r, int c, int dist, int[][] board, boolean[][] visit, int answer, int totalEmpty, int emptyCnt) {
//        pb(visit);
        if (dist >= answer) return answer;
        if (totalEmpty == emptyCnt) return dist;
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (oob(nr, nc, board)) continue;
            if (visit[nr][nc]) continue;
            if (board[nr][nc] == 1) continue;
            ArrayList<int[]> newVisits = new ArrayList<>();
            while (!oob(nr, nc, board) && !visit[nr][nc] && board[nr][nc] != 1) {
                visit[nr][nc] = true;
                newVisits.add(new int[]{nr, nc});
                emptyCnt++;
                nr += dr[i];
                nc += dc[i];
            }
            nr -= dr[i];
            nc -= dc[i];
            answer = Math.min(answer, dfs(nr, nc, dist + 1, board, visit, answer, totalEmpty, emptyCnt));
            resetVisit(visit, newVisits);
            emptyCnt = resetEmptyCnt(emptyCnt, newVisits);
        }
        return answer;
    }

    private static int resetEmptyCnt(int emptyCnt, ArrayList<int[]> newVisits) {
        emptyCnt -= newVisits.size();
        return emptyCnt;
    }

    private static void resetVisit(boolean[][] visit, ArrayList<int[]> newVisits) {
        for (int[] newVisit : newVisits) {
            int x = newVisit[0];
            int y = newVisit[1];
            visit[x][y] = false;
        }
    }

    private static boolean oob(int r, int c, int[][] board) {
        int N = board.length;
        int M = board[0].length;
        return r < 0 || r >= N || c < 0 || c >= M;
    }

    public static void pb(boolean[][] board) {
        for (int i = 0; i < board.length; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
        System.out.println();
    }
}

