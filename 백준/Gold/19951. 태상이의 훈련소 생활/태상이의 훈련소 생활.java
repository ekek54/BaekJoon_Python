import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static int N, M;
    public static int[] H;
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            H[i] = Integer.parseInt(st.nextToken());
        }
        int[] acc = new int[N + 1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            acc[a - 1] += k;
            acc[b] -= k;
        }
//        System.out.println(Arrays.toString(acc));
        for (int i = 1; i <= N; i++) {
            acc[i] += acc[i - 1];
        }
//        System.out.println(Arrays.toString(acc));
        for (int i = 0; i < N; i++) {
            H[i] += acc[i];
        }
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < N; i++) {
            answer.append(H[i]).append(' ');
        }
        System.out.println(answer);
    }
}
