import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static long D;
    static ArrayList<int[]> rules = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(leftBisec());
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        D = Long.parseLong(st.nextToken());
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int[] rule = parseRule(st);
            rules.add(rule);
        }
    }

    private static int[] parseRule(StringTokenizer st) {
        return new int[]{
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken())
        };
    }

    // n번 상자에 몇개까지 쌓이는가
    private static int leftBisec() {
        int l = 0;
        int r = N;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (D <= dCount(mid)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }

    private static long dCount(int mid) {
        long result = 0;
        for (int[] rule : rules) {
            int start, end, term;
            start = rule[0];
            end = Math.min(mid, rule[1]);
            term = rule[2];
            if (end >= start) {
                result += (end - start) / term + 1;
            }
        }
        return result;
    }
}
