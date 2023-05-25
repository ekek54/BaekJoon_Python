import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] solutions;

    public static void main(String[] args) throws IOException {
        init();
        int[] answer = twoPointer();
        System.out.println(answer[0] + " " + answer[1]);
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        solutions = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            solutions[i] = Integer.parseInt(st.nextToken());
        }
    }

    static int[] twoPointer() {
        int minValue = 2000000000;
        int[] result = new int[2];
        int l = 0;
        int r = N - 1;
        while (l < r) {
            int mixedValue = solutions[l] + solutions[r];
            if (minValue > Math.abs(mixedValue)) {
                minValue = Math.abs(mixedValue);
                result[0] = solutions[l];
                result[1] = solutions[r];
            }
            if (mixedValue <= 0) {
                l += 1;
            } else {
                r -= 1;
            }
        }
        return result;
    }
}
