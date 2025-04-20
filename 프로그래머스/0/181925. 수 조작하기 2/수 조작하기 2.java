import java.util.*;

class Solution {
    public String solution(int[] numLog) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < numLog.length - 1; i++) {
            int gap = numLog[i + 1] - numLog[i];
            if (gap == 1) {
                sb.append('w');
                continue;
            }
            if (gap == -1) {
                sb.append('s');
                continue;
            }
            if (gap == 10) {
                sb.append('d');
                continue;
            }
            if (gap == -10) {
                sb.append('a');
            }
        }
            
        return sb.toString();
    }
}