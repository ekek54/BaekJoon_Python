import java.util.*;
class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        int[] countX = new int[10];
        int[] countY = new int[10];
        int[] count = new int[10];
        for (int i = 0; i < X.length(); i++){
            countX[Character.getNumericValue(X.charAt(i))] += 1;
        }
        for (int i = 0; i < Y.length(); i++){
            countY[Character.getNumericValue(Y.charAt(i))] += 1;
        }
        for (int i = 0; i < 10; i++){
            count[i] = Math.min(countX[i], countY[i]);
        }
        System.out.println(Arrays.toString(count));
        StringBuilder sb = new StringBuilder();
        for (int i = 9; i >= 0; i--){
            for (int j = 0; j < count[i]; j ++){
                sb.append(Integer.toString(i));
                if(sb.charAt(0) == '0') break;
            }
        }
        answer = sb.toString();
        if (answer.length()== 0){
            return "-1";
        }
        return answer;
    }
}