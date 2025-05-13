import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int[] remains = new int[progresses.length];
        Stack<Integer> stack = new Stack<>();
        int acc = 0;
        for (int i = 0; i < progresses.length; i++) {
            int remain = (100 - progresses[i]) / speeds[i];
            remain += (100 - progresses[i]) % speeds[i] != 0 ? 1 : 0;
            if (stack.isEmpty()) {
                stack.add(remain);
                acc = 1;
                continue;
            }
            if (stack.peek() >= remain) {
                acc += 1;
                continue;
            }
            stack.add(remain);
            answer.add(acc);
            acc = 1;
        }
        answer.add(acc);
        return answer;
    }
}