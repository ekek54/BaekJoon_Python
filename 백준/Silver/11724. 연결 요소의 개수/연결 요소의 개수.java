import java.util.*;
import java.io.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }

        boolean[] visit = new boolean[N];
        int answer = 0;
        for (int i = 0; i < N; i++) {
            if (visit[i]) continue;
            answer += 1;
            visit[i] = true;
            Queue<Integer> que = new LinkedList<>();
            que.add(i);
            while (!que.isEmpty()) {
                int cur = que.poll();
                for (int nxt : adjList.get(cur)) {
                    if (visit[nxt]) continue;
                    visit[nxt] = true;
                    que.add(nxt);
                }
            }
        }
        System.out.println(answer);
    }
}
