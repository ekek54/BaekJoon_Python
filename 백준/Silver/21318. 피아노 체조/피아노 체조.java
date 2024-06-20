import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] levels = new int[N];
        for(int i = 0; i < N; i++) {
            levels[i] = Integer.parseInt(st.nextToken());
        }
        int[] mistakes = new int[N];
        for (int i = 0; i < N - 1; i++) {
            if (levels[i] > levels[i + 1]) {
                mistakes[i + 1] = 1;
            }else {
                mistakes[i + 1] = 0;
            }
        }
        for (int i = 1; i < N; i++) {
            int cur = mistakes[i];
            int pre = mistakes[i - 1];
            mistakes[i] = cur + pre;
        }
        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            System.out.println(solution(x, y, mistakes));
        }
    }
    public static int solution(int x, int y, int[] mistakes) {
        return mistakes[y - 1] - mistakes[x - 1];
    }
}
