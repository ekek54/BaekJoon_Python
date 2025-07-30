import java.util.*;

class Solution {
    public String solution(String s) {
        StringTokenizer st = new StringTokenizer(s);
        List<Integer> nums = new ArrayList<>();
        
        while (st.hasMoreTokens()) {
            nums.add(Integer.parseInt(st.nextToken()));
        }
        System.out.println(nums);
        int max = Collections.max(nums);
        int min = Collections.min(nums);
        StringBuilder sb = new StringBuilder();
        sb.append(min);
        sb.append(" ");
        sb.append(max);
        return sb.toString();
    }
}