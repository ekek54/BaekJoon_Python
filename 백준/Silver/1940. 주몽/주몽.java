import java.util.*;
import java.io.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        int l = 0;
        int r = arr.length - 1;
        int answer = 0;
        while (l < r) {
            int sum = arr[l] + arr[r];
            if (sum == M) {
                answer++;
                l++;
                continue;
            }
            if (sum < M) {
                l++;
                continue;
            }
            if (sum > M) {
                r--;
                continue;
            }
        }

        System.out.println(answer);
    }
}
