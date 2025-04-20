import java.util.*;

class Solution {
    public int solution(int a, int b, int c) {
        int[] chks = new int[6];
        chks[a - 1] += 1;
        chks[b - 1] += 1;
        chks[c - 1] += 1;
        int maxChk = Arrays.stream(chks).max().getAsInt();
        int answer = (a + b + c);
        if (maxChk == 1) {
            return answer;
        }
        answer *= (int)(Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2));
        if (maxChk == 2) {
            return answer;
        }
        answer *= (int)(Math.pow(a, 3) + Math.pow(b, 3) + Math.pow(c, 3));
        return answer;
    }
}