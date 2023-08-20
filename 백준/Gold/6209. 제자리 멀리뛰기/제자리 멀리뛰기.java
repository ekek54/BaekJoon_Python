import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int d, n, m;
    static int[] stones;
    public static void main(String[] args) throws IOException {
        init();
        int answer = bisec();
        System.out.println(answer);
    }


    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        d = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        stones = new int[n];
        for (int i = 0; i < n; i++) {
            stones[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(stones);
    }

    private static boolean isCrossable(int minGap) {
        int curIdx = 0;
        int removeCnt = 0;
        for (int stone : stones) {
            int gap = stone - curIdx;
            if (gap < minGap) {
                removeCnt++;
            }else {
                curIdx = stone;
            }
            if (removeCnt > m) return false;
        }
        return true;
    }

    private static int bisec() {
        int l = 0;
        int r = d;

        while (l <= r) {
            int mid = (l + r) / 2;
            if (isCrossable(mid)) l = mid + 1;
            else r = mid - 1;
        }
        return r;
    }
}
