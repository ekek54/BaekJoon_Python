class Solution {
    public int solution(int storey) {
        int answer = 0;
        int carry = 0;

        String numStr = String.valueOf(storey);
        for (int i = numStr.length() - 1; i >= 0; i--) {
            int curNum = Integer.parseInt(numStr.substring(i, i + 1));
            curNum += carry;
            //System.out.println(curNum);
            if (curNum >= 6){
                answer += 10 - curNum;
                carry = 1;
            }
            else if(curNum == 5){
                if (i > 0){
                    int nxtNum = Integer.parseInt(numStr.substring(i - 1, i));
                    if (nxtNum < 5){
                        answer += curNum;
                        carry = 0;
                    }
                    else{
                        answer += 10 - curNum;
                        carry = 1;
                    }
                }
                else{
                    answer += curNum;
                    carry = 0;
                }
            }
            else{
                answer += curNum;
                carry = 0;
            }
        }
        if (carry == 1){
            answer += 1;
        }
        return answer;
    }
}