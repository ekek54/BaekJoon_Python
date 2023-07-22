import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int K = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int P = Integer.parseInt(st.nextToken());
            ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
            for (int i = 0; i < M; i++) {
                adjList.add(new ArrayList<>());
            }
            int[] indegree = new int[M];

            for (int i = 0; i < P; i++) {
                st = new StringTokenizer(br.readLine());
                int A = Integer.parseInt(st.nextToken()) - 1;
                int B = Integer.parseInt(st.nextToken()) - 1;
                indegree[B]++;
                adjList.get(A).add(B);
            }
            System.out.println(K + " " + strahlerOrder(M, adjList, indegree));
        }
    }

    public static int strahlerOrder(int M, ArrayList<ArrayList<Integer>> adjList, int[] indegree) {
        int[] order = new int[M];
        int[] cnt = new int[M];
        Queue<Integer> que = new LinkedList<>();
        int result = 0;
        for (int i = 0; i < M; i++) {
            if (indegree[i] == 0) {
                order[i] = 1;
                que.add(i);
            }
        }
        while (!que.isEmpty()) {
            int curNode = que.poll();
            result = Math.max(result, order[curNode]);
            for (Integer nxtNode : adjList.get(curNode)) {
                if (order[nxtNode] == order[curNode]) cnt[nxtNode]++;
                else if (order[nxtNode] < order[curNode]) {
                    order[nxtNode] = order[curNode];
                    cnt[nxtNode] = 1;
                }
                if (--indegree[nxtNode] == 0) {
                    if (cnt[nxtNode] >= 2) order[nxtNode]++;
                    que.add(nxtNode);
                }
            }
        }
//        System.out.println("order = " + Arrays.toString(order));
//        System.out.println("cnt = " + Arrays.toString(cnt));
        return result;
    }
}
