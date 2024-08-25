import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static char[][] board;
    static int N;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        parseInput();
        SectionCountable colorBlind = new SectionCountable() {
            @Override
            public boolean isSameColor(char color1, char color2) {
                if (color1 == color2) {
                    return true;
                }
                if (color1 == 'R' && color2 == 'G') {
                    return true;
                }
                if (color1 == 'G' && color2 == 'R') {
                    return true;
                }
                return false;
            }
        };

        SectionCountable normal = new SectionCountable() {
            @Override
            public boolean isSameColor(char color1, char color2) {
                return color1 == color2;
            }
        };

        System.out.println(normal.countSection(board) + " " + colorBlind.countSection(board));
    }

    public static void parseInput() throws IOException {
        N = Integer.parseInt(br.readLine());
        board = new char[N][N];
        for(int i = 0; i < N; i++) {
            board[i] = br.readLine().toCharArray();
        }
    }

    public static void pb() {
        for(int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }
}

interface SectionCountable {
    default int countSection(char[][] board) {
        int N = board.length;
        boolean[][] visit = new boolean[N][N];
        int sectionCount = 0;
        for(int r = 0; r < N; r++) {
            for(int c = 0; c < N; c++) {
                if(visit[r][c]) continue;
                visit[r][c] = true;
                sectionCount++;
                dfs(r, c, board, visit);
            }
        }
        return sectionCount;
    }

    default void dfs(int r, int c, char[][] board, boolean[][] visit) {
        int N = board.length;
        int[] dr = new int[] {1, -1, 0, 0};
        int[] dc = new int[] {0, 0, 1, -1};
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {r, c});
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            for(int i = 0; i < 4; i++) {
                int nr = cur[0] + dr[i];
                int nc = cur[1] + dc[i];
                if(outOfBound(nr, nc, N) || visit[nr][nc]) continue;
                if(isSameColor(board[r][c], board[nr][nc])) {
                    visit[nr][nc] = true;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
    }

    default boolean outOfBound(int r, int c, int N) {
        return r < 0 || c < 0 || r >= N || c >= N;
    }

    boolean isSameColor(char color1, char color2);
}