import java.util.*;
class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, new Comparator<int[]>() {
            @Override
            public int compare(int[] e1, int[] e2) {
                return e1[1] - e2[1];
            }
        });

        int bound = 0;
        for (int i = 0; i < targets.length; i++) {
            if (targets[i][0] < bound) continue;
            else{
                answer ++;
                bound = targets[i][1];
            }
            //System.out.println(Arrays.toString(targets[i]));
        }
        return answer;
    }
}