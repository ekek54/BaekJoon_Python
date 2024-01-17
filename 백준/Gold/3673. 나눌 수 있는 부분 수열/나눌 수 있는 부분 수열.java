import java.util.*;
import java.io.*;

public class Main {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


    public static void main(String[] args) throws IOException {
        int c = Integer.parseInt(br.readLine());
        while (c-- > 0) {
            solution();
        }
    }

    private static void solution() throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());
        long d = Long.parseLong(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        long[] nums = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }
        long[] acc = new long[n + 1];
        for (int i = 1; i < n + 1; i++) {
            acc[i] = acc[i - 1] + nums[i - 1];
        }
        Map<Long, Integer> modCounts = new HashMap<>();
        for (int i = 0; i < n + 1; i++) {
            long mod = acc[i] % d;
            if (modCounts.containsKey(mod)) {
                int count = modCounts.get(mod);
                modCounts.put(mod, count + 1);
            } else modCounts.put(mod, 1);
        }
//        System.out.println(Arrays.toString(acc));
//        System.out.println(modCounts);
        long sum = modCounts.values().stream().mapToLong(count -> nC2(count)).sum();
        System.out.println(sum);
    }

    private static long nC2(long n) {
        return (n * (n - 1)) / 2;
    }
}
