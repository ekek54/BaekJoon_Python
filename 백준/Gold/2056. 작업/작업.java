import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[] times;
    static int[] indegrees;
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(finishAt());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        times = new int[N];
        indegrees = new int[N];
        for (int i = 0; i < N; i++) adjList.add(new ArrayList<Integer>());
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            times[i] = Integer.parseInt(st.nextToken());
            indegrees[i] = Integer.parseInt(st.nextToken());
            for (int j = 0; j < indegrees[i]; j++) {
                adjList.get(Integer.parseInt(st.nextToken()) - 1).add(i);
            }
        }
    }

    static int finishAt() {
        int result = 0;
        Queue<Integer> que = new LinkedList<>();
        int[] startAt = new int[N];
        for (int i = 0; i < N; i++) {
            if (indegrees[i] == 0) {
                que.add(i);
            }
        }
        while (!que.isEmpty()) {
            int curWork = que.poll();
            int doneAt = startAt[curWork] + times[curWork];
            result = Math.max(result, doneAt);
            for (Integer nxtWork : adjList.get(curWork)) {
                indegrees[nxtWork] -= 1;
                startAt[nxtWork] = Math.max(startAt[nxtWork], doneAt);
                if (indegrees[nxtWork] == 0) {
                    que.add(nxtWork);
                }
            }
        }
        //System.out.println(Arrays.toString(startAt));
        return result;
    }
}
