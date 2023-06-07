import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
    static int N, K;
    static int[] X;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(rightBiSec());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        X = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            X[i] = Integer.parseInt(st.nextToken());
        }
    }

    static int rightBiSec() {
        int l = 0;
        int r = 2000000;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (isSplitable(mid)) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return r;
    }

    static boolean isSplitable(int limit) {
        int acc = 0;
        int splitCnt = 0;
        for (int i = 0; i < N; i++) {
            acc += X[i];
            if (acc >= limit) {
                splitCnt++;
                acc = 0;
            }
        }
        return splitCnt >= K;
    }
}
