import java.io.*;
import java.util.*;


public class Main {
    static int N, M;
    static int[] recommends;

    private static class Frame implements Comparable{
        public int studentNum;
        public int recommendCnt;
        public int frameAt;

        public Frame(int studentNum, int frameAt) {
            this.studentNum = studentNum;
            recommendCnt = 1;
            this.frameAt = frameAt;
        }

        @Override
        public String toString() {
            return "Frame{" +
                    "studentNum=" + studentNum +
                    ", recommendCnt=" + recommendCnt +
                    ", frameAt=" + frameAt +
                    '}';
        }

        @Override
        public int compareTo(Object o) {
            if (o instanceof Frame) {
                Frame f = (Frame)o;
                if (recommendCnt == f.recommendCnt) return frameAt - f.frameAt;
                else return recommendCnt - f.recommendCnt;

            }
            throw new IllegalArgumentException();
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        PriorityQueue<Frame> pq = new PriorityQueue<>(Frame::compareTo);
        int i = 0;
        for (int recommend : recommends) {
            i++;
            boolean recommendInFrame = false;
            for (Frame frame : pq) {
                if (frame.studentNum == recommend) {
                    pq.remove(frame);
                    frame.recommendCnt++;
                    pq.add(frame);
                    recommendInFrame = true;
                    break;
                }
            }
            if (recommendInFrame) continue;

            if(pq.size() == N) pq.poll();
            pq.add(new Frame(recommend, i));
        }
        List<Integer> candidateList = new ArrayList<>();
        for (Frame frame : pq) {
            candidateList.add(frame.studentNum);
        }
        candidateList.sort(Integer::compareTo);
        StringBuilder sb = new StringBuilder();
        for (Integer candidate : candidateList) {
            sb.append(candidate).append(" ");
        }
        System.out.println(sb);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        recommends = new int[M];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            recommends[i] = Integer.parseInt(st.nextToken());
        }
    }
}
