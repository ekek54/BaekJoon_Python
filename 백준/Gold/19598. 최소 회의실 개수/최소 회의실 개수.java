import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Meeting[] meetings = new Meeting[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int finish = Integer.parseInt(st.nextToken());
            meetings[i] = new Meeting(start, finish);
        }
        Arrays.sort(meetings);
        PriorityQueue<Integer> rooms = new PriorityQueue<>();
        rooms.add(0);
        for (int i = 0; i < N; i++) {
            if (rooms.peek() <= meetings[i].start) {
                rooms.poll();
                rooms.add(meetings[i].finish);
            } else {
                rooms.add(meetings[i].finish);
            }
        }
        System.out.println(rooms.size());
    }

    static class Meeting implements Comparable<Meeting>{
        int start;
        int finish;

        public Meeting(int start, int finish) {
            this.start = start;
            this.finish = finish;
        }

        @Override
        public int compareTo(Meeting m) {
            if (this.start == m.start) {
                return this.finish - m.finish;
            }
            return this.start - m.start;
        }
    }
}
