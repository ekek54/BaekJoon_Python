import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static long N;
    static int M;
    static int[] times;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(result());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Long.parseLong(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        times = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            times[i] = Integer.parseInt(st.nextToken());
        }
    }

    static long leftBiSec() {
        long l = 0L;
        long r = 60000000000L;
        while (l <= r) {
            long mid = (l + r) / 2;
            if (isDone(mid) >= N) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }

    static long isDone(long mid) {
        long capacity = 0L;
        for (int time : times) {
            capacity += mid / time + 1;
        }
        return capacity;
    }

    static int result() {
        long doneTime = leftBiSec();
        long done = isDone(doneTime);
        long remain = done - N;
//        System.out.println("doneTime = " + doneTime);
//        System.out.println("done = " + done);
        ArrayList<Integer> match = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            if (doneTime % times[i] == 0) {
                match.add(i + 1);
            }
        }
        return match.get((int) (match.size() - 1 - remain));
    }
}
