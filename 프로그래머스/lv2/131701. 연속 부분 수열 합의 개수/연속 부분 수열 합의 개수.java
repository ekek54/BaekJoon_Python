import java.util.*;
class Solution {
    public int solution(int[] elements) {
        HashMap<Integer, Boolean> subSumMap = new HashMap<>();
        for(int i = 0; i < elements.length; i ++){
            for(int j = 0; j <= elements.length; j ++){
                subSumMap.put(sumAtoB(elements, j, j + i), true);
            }
        }
        return subSumMap.size();
    }
    
    public int sumAtoB(int[] arr, int A, int B) {
        int ret = 0;
        for(int i = A; i <= B; i++){
            ret += arr[i % arr.length];
        }
        return ret;
    }
}