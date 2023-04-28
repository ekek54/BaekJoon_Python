class Solution {
    public int solution(int num) {
        long numLong = new Long(num);
        int answer = 0;
        while (numLong != 1){
            //System.out.println(numLong);
            if (answer == 500) break;
            if (numLong % 2 == 0){
                numLong /= 2;
            }
            else{
                numLong = numLong * 3 + 1;
            }
            answer += 1;
        }
        if (answer == 500){
            return -1;
        }
        return answer;
    }
}