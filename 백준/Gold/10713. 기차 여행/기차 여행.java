import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] rails;
    static int[] P, A, B, C;

    public static void main(String[] args) throws IOException {
        init();

        for (int i = 0; i < M - 1; i++) {
            rails[Math.min(P[i], P[i + 1])] += 1;
            rails[Math.max(P[i], P[i + 1])] -= 1;
        }

        for (int i = 1; i < N; i++) {
            rails[i] += rails[i - 1];
        }

        int answer = 0;

        for (int i = 0; i < N - 1; i++) {
            answer += Math.min(rails[i] * A[i], rails[i] * B[i] + C[i]);
        }
        System.out.println(answer);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        A = new int[N - 1];
        B = new int[N - 1];
        C = new int[N - 1];
        rails = new int[N];
        P = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            P[i] = Integer.parseInt(st.nextToken()) - 1;
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
            C[i] = Integer.parseInt(st.nextToken());
        }
    }


}
