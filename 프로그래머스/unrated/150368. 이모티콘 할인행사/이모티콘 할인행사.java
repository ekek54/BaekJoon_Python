// 7가지 상품에대해 각각 4가지의 할인률을 적용할 수 있다.
// 4^7의 경우의 수 가능 = 16 * 2 ^ 10 = 16000
// 유저 한명당 결과 도출에는 각 상품을 순회(7)하여 총 구매 금액 판별 = 7 * C
// 유저는 최대 100명
// 따라서 O(16000 * 100 * 7 * C) = O(11200000)
// 타이트하지만 완탐 가능
import java.util.*;
class Solution {
    int n;
    int m;
    int[] discounts = {10, 20, 30, 40}; 
    int[][] userArr;
    int[] emoticonArr;
    int[] itemDiscount;
    int[] answer = {0, 0};
    public int[] solution(int[][] users, int[] emoticons) {
        n = users.length;
        m = emoticons.length;
        itemDiscount = new int[m];
        userArr = users;
        emoticonArr = emoticons;
        dfs(0);
        return answer;
    }

    public void dfs(int cnt){
        if (cnt == m){
            int[] result = aggregate();
            //System.out.println(Arrays.toString(answer));
            //System.out.println(Arrays.toString(result));
            if (result[0] > answer[0] || (result[0] == answer[0] && result[1] > answer[1])){
                answer = result;
            }
            return;
        }
        for (int i = 0; i < 4; i ++){
            itemDiscount[cnt] = discounts[i];
            dfs(cnt + 1);
            itemDiscount[cnt] = 0;
        }
    }
    
    public int[] aggregate(){
        int[] ret = {0, 0};
        for(int i = 0; i < n; i ++){
            int reqDiscount = userArr[i][0];
            int limitPrice = userArr[i][1];
            int totalUsed = 0;
            for (int j = 0; j < m; j ++){
                if (itemDiscount[j] < reqDiscount) continue;
                totalUsed += emoticonArr[j] * (100 - itemDiscount[j]) / 100;
            }
            if (totalUsed >= limitPrice){
                ret[0] += 1;
            }
            else{
                ret[1] += totalUsed;
            }
        }
        return ret;
    }
}