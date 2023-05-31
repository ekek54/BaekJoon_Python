import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, K;
    static int[] springwaters;
    static Map<Integer, Boolean> visit;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(bfs());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        springwaters = new int[N];
        visit = new HashMap<>();
        for (int i = 0; i < N; i++) {
            springwaters[i] = Integer.parseInt(st.nextToken());
        }
    }

    static long bfs() {
        long result = 0L;
        int homeCount = 0;
        Queue<int[]> que = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            que.add(new int[]{springwaters[i], 0});
            visit.put(springwaters[i], true);
        }
        while (!que.isEmpty()) {
            int[] cur = que.poll();
            int curX = cur[0];
            int curUnhappiness = cur[1];
            if (curUnhappiness != 0) {
                homeCount += 1;
                result += curUnhappiness;
            }
            if (homeCount == K) {
                break;
            }
            if (!visit.containsKey(curX - 1)) {
                que.add(new int[]{curX - 1, curUnhappiness + 1});
                visit.put(curX - 1, true);
            }
            if (!visit.containsKey(curX + 1)) {
                que.add(new int[]{curX + 1, curUnhappiness + 1});
                visit.put(curX + 1, true);
            }
        }
        return result;
    }

}
