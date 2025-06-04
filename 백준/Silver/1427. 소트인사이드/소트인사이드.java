import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        String N = br.readLine();
        int[] arr = new int[N.length()];
        for (int i = 0; i < N.length(); i++) {
            arr[i] = Integer.parseInt(String.valueOf(N.charAt(i)));
        }
        for (int i = 0; i < N.length(); i++) {
            for (int j = i + 1; j < N.length(); j++) {
                if (arr[i] < arr[j]) {
                    int tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int a : arr) {
            sb.append(a);
        }
        System.out.println(sb);
    }
}
