import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Collections.reverseOrder());
    static PriorityQueue<Integer> minPQ = new PriorityQueue<>();
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());

            if (maxPQ.isEmpty()) {
                maxPQ.add(num);
                sb.append(maxPQ.peek()).append("\n");
                continue;
            }

            if (maxPQ.peek() >= num) {
                maxPQ.add(num);
            }else{
                minPQ.add(num);
            }

            if (maxPQ.size() - minPQ.size() > 1) {
                minPQ.add(maxPQ.poll());
            } else if (maxPQ.size() < minPQ.size()) {
                maxPQ.add(minPQ.poll());
            }
            sb.append(maxPQ.peek()).append("\n");
        }

        System.out.println(sb);
    }
}
