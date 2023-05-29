import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] lectures;

    public static void main(String[] args) throws IOException{
        init();
        System.out.println(simulation());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        lectures = new int[N][2];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            lectures[i][0] = Integer.parseInt(st.nextToken());
            lectures[i][1] = Integer.parseInt(st.nextToken());
        }
    }

    static int simulation() {
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            return o1[1] - o2[1];
        });
        Arrays.sort(lectures, (o1, o2) -> o1[0] - o2[0]);
        int result = 0;
        int roomInUse = 0;
        for (int[] lecture : lectures) {
            int start = lecture[0];
            if (!pq.isEmpty()) {
                if (pq.peek()[1] <= start) {
                    pq.poll();
                    roomInUse -= 1;
                }
            }
            pq.add(lecture);
            roomInUse += 1;
            result = Math.max(result, roomInUse);
        }
        return result;
    }
}
