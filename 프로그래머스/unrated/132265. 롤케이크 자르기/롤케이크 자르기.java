import java.util.*;
class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < topping.length; i ++) {
            if (map.containsKey(topping[i])) {
                map.put(topping[i], map.get(topping[i]) + 1);
            }
            else{
                map.put(topping[i], 1);
            }
        }
        
        HashMap<Integer, Integer> remain = new HashMap<>();
        for(int i = 0; i < topping.length; i ++) {
            // A에서 제외
            if (map.get(topping[i]) == 1){
                map.remove(topping[i]);
            }
            else{
                map.put(topping[i], map.get(topping[i]) - 1);
            }
            // B에 추가
            if (remain.containsKey(topping[i])){
                remain.put(topping[i], remain.get(topping[i]) + 1);
            }
            else{
                remain.put(topping[i], 1);
            }
            
            if (map.size() == remain.size()){
                answer += 1;
            }
        }
        return answer;
    }
}