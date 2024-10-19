import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N;
    private static List<Problem> problems = new ArrayList<>();
    private static int[] parent;
    private static Problem[] schedule;

    public static void main(String[] args) throws IOException{
        readInput();
        initParent();
        schedule = new Problem[N];
        for (Problem problem: problems) {
            int emptyIdx = find(problem.deadline - 1);
            if (emptyIdx != -1) {
                schedule[emptyIdx] = problem;
                union(emptyIdx, emptyIdx - 1);
            } else {
                continue;
            }
        }
        int answer = 0;
        for (Problem problem: schedule) {
            if (problem != null) {
                answer += problem.reward;
            }
        }
        // System.out.println(Arrays.toString(schedule));
        System.out.println(answer);
    }

    private static int find(int a) {
        if (a == -1) return -1;
        if (a == parent[a]) {
            return a;
        } else {
            parent[a] = find(parent[a]);
            return parent[a];
        }
    }

    private static boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a < b) {
            parent[b] = a;
            return true;
        } else if(a > b) {
            parent[a] = b;
            return true;
        }
        return false;
    }

    private static void initParent() {
        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }
    }

    private static void readInput() throws IOException {
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            problems.add(new Problem(a, b));
        }
        problems.sort((a, b) -> {
            if (a.reward == b.reward) {
                return b.deadline - a.deadline;
            } else {
                return b.reward - a.reward;
            }
        });
    }
}

class Problem {
    public int deadline;
    public int reward;

    public Problem(int deadline, int reward) {
        this.deadline = deadline;
        this.reward = reward;
    }

    @Override
    public String toString() {
        return "{" + "\n\tdeadline: " + deadline + "\n\treward: " + reward + "\n}";
    }
}
