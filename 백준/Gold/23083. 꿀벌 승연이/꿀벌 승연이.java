import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
	private static long[][] board, dp;
	private static int N, M, K;
	public static void main(String[] args) throws IOException {
		input();
		pro();
		System.out.println(dp[N][M] % 1_000_000_007);
	}
	private static void pro() {
		initialDp();
		for (int col = 2; col <= M; col++) {
			for (int row = 1; row <= N; row++) {
				// 빈칸은 못감
				if (board[row][col] == 1) {
					dp[row][col] = 0;
					continue;
				}
				// (row,col)로의 경로개수 = 위칸의 경로개수 + 왼쪽상단의 경로개수 + 왼쪽하단의 경로개수 (col이 홀, 짝에 따라 점화식이 다름)
				if (col % 2 == 0) {
					dp[row][col] = dp[row - 1][col] + dp[row][col - 1] + dp[row + 1][col - 1];
				} else {
					dp[row][col] = dp[row - 1][col] + dp[row - 1][col - 1] + dp[row][col - 1];
				}
                dp[row][col] = dp[row][col] % 1_000_000_007;
			}
		}
	}
	private static void initialDp() {
		dp = new long[N + 2][M + 2];
		// 수정전: 1열은 모두 1이다
		// 수정후: row행 1열에 구멍이있으면 이 후의 row행 1열은 갈 수 없다.
		for (int row = 1; row <= N; row++) {
			if(board[row][1] == 1) {
				break;
			}
			dp[row][1] = 1;
		}
	}
	private static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new long[N + 2][M + 2];
		st = new StringTokenizer(br.readLine());
		K = Integer.parseInt(st.nextToken());
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			int row = Integer.parseInt(st.nextToken());
			int col = Integer.parseInt(st.nextToken());
			board[row][col] = 1;
		}
	}
}