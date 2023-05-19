import java.util.*;

public class Main {
    static int N, M, K;
    static int[][] scoreMatrix;

    static int[][] dist;

    static final int INF = 10000 * 300;

    public static void main(String[] args) {
        init();
        System.out.println(solution());
    }

    public static void init() {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        dist = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                dist[i][j] = -INF;
            }
        }
        dist[0][0] = 0;
        scoreMatrix = new int[N][N];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(sc.nextLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());
            if (a < b) {
                if (scoreMatrix[a][b] < c) {
                    scoreMatrix[a][b] = c;
                }
                if (a == 0) dist[b][1] = Math.max(dist[b][1], c);
            }
        }
    }

    public static int topDown(int i, int j) {
        if (dist[i][j] != -INF) return dist[i][j];
        if (j == 0) return -1;
        int result = 0;
        for (int k = 0; k < i; k++) {
            if (scoreMatrix[k][i] != 0) {
                int tmp = topDown(k, j - 1);
                if (tmp > 0){
                    result = Math.max(result, topDown(k, j - 1) + scoreMatrix[k][i]);
                }
            }
        }
        dist[i][j] = result;
        return result;
    }

    public static int solution() {
        int result = 0;
        for(int i = 0; i < M; i++){
            result = Math.max(result, topDown(N - 1, i));
        }
        return result;
    }
}

