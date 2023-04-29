import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> count_map = new HashMap<>();
        for (int i = 0; i < tangerine.length; i++){
            if (count_map.containsKey(tangerine[i])){
                count_map.put(tangerine[i], count_map.get(tangerine[i]) + 1);
            }
            else{
                count_map.put(tangerine[i], 1);
            }
        }
        Integer[] counts = new Integer[count_map.size()];
        int index = 0;
        for(int count : count_map.values()){
            counts[index] = count;
            index++;
        }
        Arrays.sort(counts, Collections.reverseOrder());
        for (int i = 0; i < counts.length; i ++){
            k -= counts[i];
            answer += 1;
            if (k <= 0){
                break;
            }
                
        }
        return answer;
    }
}