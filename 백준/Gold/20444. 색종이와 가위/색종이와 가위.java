import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static long k;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(isPossible() ? "YES" : "NO");
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Long.parseLong(st.nextToken());
    }

    static boolean isPossible() {
        long l = 0;
        long r = n / 2;
        while (l <= r) {
            long x = (l + r) / 2;
            long y = n - x;
            long xy = (x + 1) * (y + 1);
            if (xy == k) {
                return true;
            }
            else if(xy < k) {
                l = x + 1;
            }
            else {
                r = x - 1;
            }
        }
        return false;
    }

}
