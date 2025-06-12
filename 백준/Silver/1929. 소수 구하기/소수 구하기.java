import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        boolean[] e = new boolean[N + 1];
        e[0] = true;
        e[1] = true;
        for (int i = 2; i <= (int)Math.sqrt(N); i++) {
            int j = 2;
            while (i * j <= N) {
                e[i * j] = true;
                j++;
            }
        }
        int answer = 0;
        for (int i = M; i <= N; i++) {
            if (!e[i]) {
                System.out.println(i);
            }
        }
    }
}