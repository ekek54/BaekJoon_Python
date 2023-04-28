import java.util.*;
class Solution {
    public String solution(int[] food) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i < food.length; i ++){
            for (int j = 0; j < food[i] / 2; j++){
                sb.append(Integer.toString(i));
            }
        }
        StringBuilder rev_sb = new StringBuilder(sb);
        sb.append('0');
        sb.append(rev_sb.reverse().toString());
        return sb.toString();
    }
}