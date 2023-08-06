import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static int[] H;
    static Stack<Integer> stack = new Stack<>();
    static Set<Integer> answerSet = new HashSet<>();

    public static void main(String[] args) throws IOException {
        init();
        dfs(0);
        StringBuilder sb = new StringBuilder();
        answerSet.stream().sorted().forEach(answer -> sb.append(answer).append(' '));
        System.out.println(answerSet.isEmpty() ? -1 : sb);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            H[i] = Integer.parseInt(st.nextToken());
        }
    }

    private static void dfs(int cnt) {
        if (cnt == M) {
//            System.out.println("stack = " + stack);
            int sum = stack.stream().mapToInt(i -> H[i]).sum();
            if (isPrime(sum)) answerSet.add(sum);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!stack.isEmpty() && i <= stack.peek()) continue;
            stack.add(i);
            dfs(cnt + 1);
            stack.pop();
        }
    }

    private static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= (int)Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
