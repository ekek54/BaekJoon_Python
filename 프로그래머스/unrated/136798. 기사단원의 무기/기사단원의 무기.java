import java.util.*;
class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i = 0; i < number; i++){
            int reqWeapon = 0;
            for (int j = 1; j <= Math.sqrt(i + 1); j++){
                if((i + 1) % j == 0){
                    if((i + 1) / j == j){
                        reqWeapon += 1;
                    }
                    else{
                        reqWeapon += 2;
                    }
                }
            }
            if (reqWeapon > limit){
                reqWeapon = power;
            }
            answer += reqWeapon;
        }
        return answer;
    }
}