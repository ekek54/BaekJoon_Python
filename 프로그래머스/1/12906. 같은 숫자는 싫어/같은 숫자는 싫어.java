import java.util.*;

public class Solution {
    public Integer[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        for (int num : arr) {
            if (stack.isEmpty()) {
                stack.add(num);
                continue;
            }
            if (stack.peek() == num) continue;
            stack.add(num);
        }
        return stack.toArray(new Integer[stack.size()]);
    }
}