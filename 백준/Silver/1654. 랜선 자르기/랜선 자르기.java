import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int K, N;
    static long[] cables;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(bisecRight());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        cables = new long[K];
        for (int i = 0; i < K; i++) {
            cables[i] = Long.parseLong((br.readLine()));
        }
    }

    static long bisecRight() {
        long l = 0;
        long r = Integer.MAX_VALUE;
        while (l <= r) {
            long mid = (l + r) / 2;
//            System.out.println("mid = " + mid);
            if (splitAs(mid) < N) {
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
        return r;
    }

    static long splitAs(long mod) {
        long result = 0;
        for (long cable : cables) {
            result += cable / mod;
        }
        return result;
    }
}
