import java.util.*;
import java.io.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Integer[] coins = new Integer[N];
        
        for (int i = 0; i < N; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(coins, Collections.reverseOrder());
        int answer = 0;
        for (int coin: coins) {
            answer += K / coin;
            K %= coin;
        }
        System.out.println(answer);
    }
}