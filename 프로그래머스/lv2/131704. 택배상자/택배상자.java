import java.util.*;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Stack<Integer> stack = new Stack<Integer>();
        int idx = 0;
        for (int i = 1; i <= order.length; i++) {
            while (!stack.empty()) {
                if (stack.peek() == order[idx]) {
                    stack.pop();
                    answer += 1;
                    idx += 1;
                }
                else break;
            }
            if (i == order[idx]){
                answer += 1;
                idx += 1;
            }
            else{
                stack.push(i);
            }
        }

        while (!stack.empty()) {
            if (stack.peek() == order[idx]) {
                stack.pop();
                answer += 1;
                idx += 1;
            }
            else break;
        }

        return answer;
    }
}