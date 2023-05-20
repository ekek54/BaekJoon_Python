import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int C;
    static int[] X;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(rightBiSec());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        X = new int[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            X[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(X);
    }

    static boolean isCutable(int n) {
        int remain = C - 1;
        int preIdx = 0;
        for (int i = 1; i < N; i++) {
            if (X[i] - X[preIdx] >= n) {
                remain -= 1;
                preIdx = i;
            }
        }
        return remain <= 0;
    }

    static int rightBiSec() {
        int l = 1;
        int r = X[X.length - 1] - X[0];
        while (l <= r) {
            int mid = (l + r) / 2;
            if (isCutable(mid)) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return r;
    }
}
