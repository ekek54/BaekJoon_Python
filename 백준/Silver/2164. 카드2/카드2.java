import java.util.*;
import java.io.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static Queue<Integer> que = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        for (int i = 1; i <= N; i++) {
            que.add(i);
        }

        while (que.size() > 1) {
            que.poll();
            que.add(que.poll());
        }

        System.out.println(que.poll());
    }
}
