import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static PriorityQueue<Problem> maxHeap = new PriorityQueue<>((p1, p2)->{
        if (p1.getDifficulty() == p2.getDifficulty()) return p2.getNumber() - p1.getNumber();
        return p2.getDifficulty() - p1.getDifficulty();
    });
    static PriorityQueue<Problem> minHeap = new PriorityQueue<>((p1, p2)->{
        if (p1.getDifficulty() == p2.getDifficulty()) return p1.getNumber() - p2.getNumber();
        return p1.getDifficulty() - p2.getDifficulty();
    });
    static Map<Integer, Integer> problemMap = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            int difficulty = Integer.parseInt(st.nextToken());
            add(number, difficulty);
        }
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            switch (command) {
                case "add": {
                    int number = Integer.parseInt(st.nextToken());
                    int difficulty = Integer.parseInt(st.nextToken());
                    add(number, difficulty);
                    break;
                }

                case "recommend":{
                    int type = Integer.parseInt(st.nextToken());
                    System.out.println(recommend(type == 1 ? maxHeap : minHeap).getNumber());
                    break;
                }

                case "solved": {
                    int number = Integer.parseInt(st.nextToken());
                    solved(number);
                    break;
                }

                default: {
                }
            }
        }

    }

    private static void add(int number, int difficulty) {
        Problem problem = new Problem(number, difficulty);
        maxHeap.add(problem);
        minHeap.add(problem);
        problemMap.put(problem.getNumber(), problem.difficulty);
    }

    private static void solved(int number) {
        problemMap.remove(number);
    }

    private static Problem recommend(PriorityQueue<Problem> problemQueue) {
        Problem peek = problemQueue.peek();
        while ((!problemQueue.isEmpty()) && (!problemMap.containsKey(peek.getNumber()) || problemMap.get(peek.getNumber()) != peek.getDifficulty())) {
            problemQueue.poll();
            peek = problemQueue.peek();
        }
        return peek;
    }

    private static class Problem {
        private final int number;
        private int difficulty;

        public Problem(int number) {
            this.number = number;
        }

        public Problem(int number, int difficulty) {
            this.number = number;
            this.difficulty = difficulty;
        }

        public int getNumber() {
            return number;
        }


        public int getDifficulty() {
            return difficulty;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Problem problem = (Problem) o;
            return number == problem.number;
        }

        @Override
        public int hashCode() {
            return Objects.hash(number);
        }

        @Override
        public String toString() {
            return "Problem{" +
                    "number=" + number +
                    ", difficulty=" + difficulty +
                    '}';
        }
    }
}
