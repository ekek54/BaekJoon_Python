import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N, M, A, B, K, G;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        init(br, st);
        int[] visitNodesOfG = new int[G];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < G; i++) {
            visitNodesOfG[i] = Integer.parseInt(st.nextToken()) - 1;
        }

        int[][] adjMatrix = new int[N][N];
        int[][] enterControlStartTime = new int[N][N];
        int[][] enterControlEndime = new int[N][N];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int U = Integer.parseInt(st.nextToken()) - 1;
            int V = Integer.parseInt(st.nextToken()) - 1;
            int L = Integer.parseInt(st.nextToken());
            adjMatrix[U][V] = L;
            adjMatrix[V][U] = L;
        }

        int timeOfG = 1;
        for (int i = 0; i < G - 1; i++) {
            int enterTime = timeOfG;
            int exitTime = enterTime + adjMatrix[visitNodesOfG[i]][visitNodesOfG[i + 1]] - 1;
            timeOfG = exitTime + 1;
            enterControlStartTime[visitNodesOfG[i]][visitNodesOfG[i + 1]] = enterTime;
            enterControlStartTime[visitNodesOfG[i + 1]][visitNodesOfG[i]] = enterTime;
            enterControlEndime[visitNodesOfG[i]][visitNodesOfG[i + 1]] = exitTime;
            enterControlEndime[visitNodesOfG[i + 1]][visitNodesOfG[i]] = exitTime;
        }
        int[] time = new int[N];
        for (int i = 0; i < N; i++) {
            time[i] = Integer.MAX_VALUE;
        }
        PriorityQueue<State> pq = new PriorityQueue<>((o1, o2) -> {
            return o1.time - o2.time;
        });
        time[A] = 1 + K;
        pq.add(new State(A, time[A]));
        while (!pq.isEmpty()) {
            State curState = pq.poll();
            if (time[curState.curNode] < curState.time) continue;

            for (int i = 0; i < N; i++) {
                if (adjMatrix[curState.curNode][i] == 0) continue;
                if (
                        0 < enterControlStartTime[curState.curNode][i]
                        && enterControlStartTime[curState.curNode][i] <= curState.time
                        && curState.time <= enterControlEndime[curState.curNode][i]
                ) {
                    int arriveTime = enterControlEndime[curState.curNode][i] + 1 + adjMatrix[curState.curNode][i];

                    if (time[i] > arriveTime) {
                        time[i] = arriveTime;
                        pq.add(new State(i, time[i]));
                    }
                } else {
                    if (time[i] > curState.time + adjMatrix[curState.curNode][i]) {
                        time[i] = curState.time + adjMatrix[curState.curNode][i];
                        pq.add(new State(i, time[i]));
                    }
                }
            }
        }

        System.out.println(time[B] - time[A]);
    }

    public static class State {
        public final int curNode;
        public final int time;

        public State(int curNode, int time) {
            this.curNode = curNode;
            this.time = time;
        }
    }

    private static void init(BufferedReader br, StringTokenizer st) throws IOException {
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken()) - 1;
        B = Integer.parseInt(st.nextToken()) - 1;
        K = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
    }

    static void printBoard(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            System.out.println(Arrays.toString(board[i]));

        }
    }
}

