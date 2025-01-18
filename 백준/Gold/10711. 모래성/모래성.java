import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int H, W;
    private static int[][] board;
    private static final int[] dr = new int[] {-1, -1, -1, 0, 0, 1, 1, 1};
    private static final int[] dc = new int[] {-1, 0, 1, -1, 1, -1, 0, 1};
    private static final int DIRECTION_COUNT = 8;

    public static void main(String[] args) throws IOException {
        parseInput();
//        printBoard();
        solution();
    }

    private static void printBoard() {
        for (int i = 0; i < H; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }

    private static void parseInput() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        board = new int[H][W];
        for (int i = 0; i < H; i++) {
            String input = br.readLine();
            for (int j = 0; j < W; j++) {
                if (input.charAt(j) == '.') {
                    board[i][j] = 0;
                } else {
                    board[i][j] = Character.getNumericValue(input.charAt(j));
                }
            }
        }
    }

    private static void solution() {
        int answer = 0;
        Queue<State> que = new LinkedList<>();
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (board[i][j] == 0) {
                    que.add(new State(i, j, 0));
                }
            }
        }

        while (!que.isEmpty()) {
            State cur = que.poll();
            answer = Math.max(answer, cur.s);
            for (int i = 0; i < DIRECTION_COUNT; i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];
                if (oob(nr, nc)) continue;
                if (board[nr][nc] == 0) continue;
                if (--board[nr][nc] == 0) {
                    que.add(new State(nr, nc, cur.s + 1));
                }
            }
        }
        System.out.println(answer);
    }

    private static boolean oob(int r, int c) {
        return r < 0 || H <= r || c < 0 || W <= c;
    }

    static class State {
        public int r, c, s;

        public State (int r, int c, int s) {
            this.r = r;
            this.c = c;
            this.s = s;
        }
    }
}
