import java.util.*;

class Solution {
    public static Stack<Integer> stack = new Stack<>();
    public static int K, N;
    public static int[][] requires;
    public static int answer = Integer.MAX_VALUE;
        
    public int solution(int k, int n, int[][] reqs) {
        init(k, n, reqs);
        dfs(0);
        return answer;
    }
    
    private void init(int k, int n, int[][] reqs) {
        K = k;
        N = n;
        requires = reqs;
    }
    
    private void dfs(int cnt) {
        if (cnt == N - K) {
            int[] typeCounts = countMentoType();
            List<PriorityQueue<Integer>> mentoPQList = createMentoPQList(typeCounts);
            answer = Math.min(answer, simulation(mentoPQList));
            return;
        }
        
        for(int i = 0; i < K; i++) {
            if (!stack.isEmpty() && stack.peek() > i) continue;
            stack.add(i);
            dfs(cnt + 1);
            stack.pop();
        }
    }
    
    private List<PriorityQueue<Integer>> createMentoPQList(int[] typeCounts) {
        List<PriorityQueue<Integer>> mentoPQList = new ArrayList<>();
        for(int i = 0; i < K; i++) {
            PriorityQueue<Integer> mentoPQ = new PriorityQueue<>();
            mentoPQList.add(mentoPQ);
            for (int j = 0; j < typeCounts[i]; j++) {
                mentoPQ.add(0);
            }
        }
        return mentoPQList;
    }
    
    private int[] countMentoType() {
        int[] typeCounts = new int[K];
        Arrays.fill(typeCounts, 1);
        for (Integer type: stack) {
            typeCounts[type]++; 
        }
        return typeCounts;
    }
    
    private int simulation(List<PriorityQueue<Integer>> mentoPQList) {
        int waitTime = 0;
        for(int i = 0; i < requires.length; i++) {
            int[] req = requires[i];
            int startTime = req[0];
            int mentoringTime = req[1];
            int reqMentoType = req[2] - 1;
            PriorityQueue<Integer> mentoPQ = mentoPQList.get(reqMentoType);
            int mentoFreeAt = mentoPQ.poll();
            if (mentoFreeAt > startTime) {
                waitTime += mentoFreeAt - startTime;
                mentoFreeAt += mentoringTime;
            }else{
                mentoFreeAt = startTime + mentoringTime;
            }
            mentoPQ.add(mentoFreeAt);
        }
        return waitTime;
    }
}