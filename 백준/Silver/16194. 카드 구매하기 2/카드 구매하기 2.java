import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int N;
    private static List<Integer> P;

    public static void main(String[] args) throws IOException {
        parseInput();
        System.out.println(solution());
    }

    private static void parseInput() throws IOException {
        N = Integer.parseInt(br.readLine());
        P = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
    }

    private static int solution() {
        List<Integer> dp = new ArrayList<>();
        dp.add(P.get(0));
        for (int i = 1; i < N; i++) {
            int minVal = P.get(i);
            for (int j = 0; j < i; j++) {
                minVal = Math.min(minVal, dp.get(j) + P.get(i - j - 1));
            }
            dp.add(minVal);
        }
//        System.out.println(dp);
        return dp.get(N - 1);
    }
}
