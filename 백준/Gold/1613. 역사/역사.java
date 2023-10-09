import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, k;
    static List<Set<Integer>> laterSetList = new ArrayList<>();
    static List<List<Integer>> adjList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();

        findLater();
//        System.out.println(laterSetList);

        answer();
    }

    private static void answer() throws IOException {
        int s = Integer.parseInt(br.readLine());
        for (int i = 0; i < s; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            if (laterSetList.get(a).contains(b)) System.out.println(-1);
            else if (laterSetList.get(b).contains(a)) System.out.println(1);
            else System.out.println(0);
        }
    }

    private static void findLater() {
        for (int i = 0; i < n; i++) {
            Queue<Integer> que = new LinkedList<>();
            que.add(i);
            boolean[] visit = new boolean[n];
            Set<Integer> laterSet = laterSetList.get(i);
            while (!que.isEmpty()) {
                int cur = que.poll();
                for (Integer nxt : adjList.get(cur)) {
                    if (visit[nxt]) continue;
                    laterSet.add(nxt);
                    que.add(nxt);
                    visit[nxt] = true;
                }
            }
        }
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
            laterSetList.add(new HashSet<>());
        }

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            adjList.get(a).add(b);
        }
    }
}
