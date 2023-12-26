import java.util.*;

class Solution {
    private int n, m;
    private int idx = 0;
    
    public int solution(int[][] land) {
        n = land.length;
        m = land[0].length;
        int[][] landWithIndex = indexingLand(land);
        // pb(landWithIndex);
        int[] areas = areas(landWithIndex);
        // System.out.println(Arrays.toString(areas));
        int answer = 0;
        for (int i = 0; i < m; i++) {
            boolean[] visit = new boolean[idx + 1];
            int gain = 0;
            for (int j = 0; j < n; j++) {
                if (!visit[landWithIndex[j][i]]){
                    visit[landWithIndex[j][i]] = true;
                    gain += areas[landWithIndex[j][i]];
                }
            }
            answer = Math.max(answer, gain);
        }
        return answer;
    }
    
    private int[][] indexingLand(int[][] land) {
        int[][] result = new int[n][m];
        int[] dr = new int[] {1, -1, 0 ,0};
        int[] dc = new int[] {0 ,0, 1, -1};
        for(int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (land[i][j] == 1 && result[i][j] == 0) {
                    idx++;
                    Queue<Coordinate> que = new LinkedList<>();
                    que.add(new Coordinate(i, j));
                    result[i][j] = idx;
                    while (!que.isEmpty()) {
                        Coordinate curRC = que.poll();
                        for (int k = 0; k < 4; k++) {
                            int nr = curRC.r + dr[k];
                            int nc = curRC.c + dc[k];
                            if (nr < 0 || n <= nr || nc < 0 || m <= nc) continue;
                            if (land[nr][nc] == 1 && result[nr][nc] == 0) {
                                result[nr][nc] = idx;
                                que.add(new Coordinate(nr, nc));
                            }
                        }
                    }
                }
            }
        }
        return result;
    }
    
    private int[] areas(int[][] landWithIndex) {
        int[] result = new int[idx + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (landWithIndex[i][j] != 0) {
                    result[landWithIndex[i][j]]++;
                }
            }
        }
        return result;
    }
    
    private void pb(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }
}

class Coordinate {
    public int r;
    public int c;
    
    Coordinate(int r, int c) {
        this.r = r;
        this.c = c;
    }
}