import java.util.*;
import java.io.*;

class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int ans = 1;
        for (int i = N; i > N - M; i--) {
            ans *= i;
        }
        for (int i = 1; i <= M; i++) {
            ans /= i;
        }
        System.out.println(ans);
    }
}