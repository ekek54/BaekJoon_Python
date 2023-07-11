import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int N, K;
    public static int[] A;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        int answer = N;
        for (int i = 0; i < N; i++) {
            int l = i;
            int r = i;
            int lnum = A[i];
            int rnum = A[i];
            int cnt = 0;
            boolean outer_continue_flag = false;
            while (l > 0) {
                l -= 1;
                lnum -= K;
                if (lnum < 1) {
                    outer_continue_flag = true;
                    break;
                }
                if (A[l] != lnum) {
                    cnt++;
                }
            }
            if (outer_continue_flag) continue;
            while (r < N - 1) {
                r += 1;
                rnum += K;
                if (A[r] != rnum) {
                    cnt++;
                }
            }
//            System.out.println(cnt);
            answer = Math.min(answer, cnt);
        }
        System.out.println(answer);
    }
}
