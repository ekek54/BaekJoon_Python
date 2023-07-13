import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static int N;
    public static long[] A, B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        A = new long[N];
        B = new long[N];
        initArr(A, br);
        initArr(B, br);
        StringBuilder sb = new StringBuilder();
        for (int e : solution()) {
            sb.append(e).append(" ");
        }
        System.out.println(sb);
    }

    private static void initArr(long[] a, BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            a[i] = Long.parseLong(st.nextToken());
        }
    }

    private static int[] solution() {
        int[] result = new int[N];
        for (int i = 0; i < N; i++) {
            int possibleTileCnt = bisecRight(A[i]) - (i + 1);
            result[i] = Math.max(possibleTileCnt, 0);
        }
        return result;
    }

    private static int bisecRight(long A) {
        int l = 0;
        int r = N - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (B[mid] > A) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}
