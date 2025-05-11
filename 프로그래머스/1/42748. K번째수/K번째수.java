import java.util.*;

class Solution {
    private int[] array;
    
    public List<Integer> solution(int[] array, int[][] commands) {
        this.array = array;
        List<Integer> answer = new ArrayList<>();
        for (int[] command: commands) {
            answer.add(kNum(command));
        }
        return answer;
    }
    
    private int kNum(int[] command) {
        int i = command[0] - 1;
        int j = command[1];
        int k = command[2] - 1;
        int[] subArr = Arrays.copyOfRange(array, i, j);
        Arrays.sort(subArr);
        return subArr[k];
        
    }
}