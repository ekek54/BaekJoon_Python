import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int[][] parent;

    static int[] indegrees;

    public static void main(String[] args) throws IOException{
        init();
        System.out.println(bfs());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        parent = new int[n][2];
        indegrees = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i][0] = -1;
        }
        StringTokenizer st;
        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int w = Integer.parseInt(st.nextToken());
            parent[c][0] = p;
            parent[c][1] = w;
            indegrees[p]++;
        }
    }

    static int bfs() {
        int result = 0;
        int[] accW = new int[n];
        int[][] maxW = new int[n][2];
        Queue<Integer> que = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegrees[i] == 0) {
                que.add(i);
            }
        }
        while (!que.isEmpty()) {
            int curNode = que.poll();
            result = Math.max(result, maxW[curNode][0] + maxW[curNode][1]);
            //System.out.println(curNode);
            int parentNode = parent[curNode][0];
            if (parentNode == -1) break;
            int wToParent = parent[curNode][1];
            accW[parentNode] = Math.max(accW[parentNode], accW[curNode] + wToParent);

            if (maxW[parentNode][1] <= accW[curNode] + wToParent){
                maxW[parentNode][0] = maxW[parentNode][1];
                maxW[parentNode][1] = accW[curNode] + wToParent;
            }else if(maxW[parentNode][0] < accW[curNode] + wToParent) {
                maxW[parentNode][0] = accW[curNode] + wToParent;
            }

            if (--indegrees[parentNode] == 0) {
                que.add(parentNode);
            }
        }
        //System.out.println(Arrays.toString(accW));
        //System.out.println(Arrays.toString(maxW));
        return result;
    }
}
