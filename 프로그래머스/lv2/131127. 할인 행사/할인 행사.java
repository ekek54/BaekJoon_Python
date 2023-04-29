import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        HashMap<String, Integer> bucket = new HashMap<String, Integer>();
        // 10일치 카운팅
        for(int i = 0; i < 10; i ++){
            if(bucket.containsKey(discount[i])){
                bucket.put(discount[i], bucket.get(discount[i]) + 1);
            }
            else{
            bucket.put(discount[i], 1);
            }
        }
        for(int i = 10; i < discount.length; i ++){
            if (check(want, number, bucket)){
                answer += 1;
            }
            // 다음날 아이템 추가
            if(bucket.containsKey(discount[i])){
                bucket.put(discount[i], bucket.get(discount[i]) + 1);
            }
            else{
            bucket.put(discount[i], 1);
            }
            // 다음날 아이템 삭제
            bucket.put(discount[i - 10], bucket.get(discount[i - 10]) - 1);
        }
        if (check(want, number, bucket)){
                answer += 1;
            }
        return answer;
    }
    
    public boolean check(String[] want, int[] number, HashMap<String, Integer> bucket){
        for(int i = 0; i < want.length; i ++){
            if (!bucket.containsKey(want[i]) || bucket.get(want[i]) != number[i]){
                return false;
            }
        }
        return true;
    }
}