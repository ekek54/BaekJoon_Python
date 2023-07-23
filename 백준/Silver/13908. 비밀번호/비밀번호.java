import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int answer = 0;
    static int n, m;
    static int[] mustHaveNums;
    static int[] count = new int[10];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        mustHaveNums = new int[m];
        if (m != 0) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                mustHaveNums[i] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(0);
        System.out.println(answer);
    }

    public static void dfs(int cnt) {
        if (cnt == n) {
            if (isValid()) answer++;
            return;
        }

        for (int i = 0; i < 10; i++) {
            count[i]++;
            dfs(cnt + 1);
            count[i]--;
        }
    }

    public static boolean isValid() {
        for (int mustHaveNum : mustHaveNums) {
            if (count[mustHaveNum] == 0) return false;
        }
        return true;
    }
}
