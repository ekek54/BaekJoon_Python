class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int idx = 0;
        int idx1 = 0;
        int idx2 = 0;
        while (idx < goal.length){
            //System.out.println(goal[idx]);
            if (idx1 < cards1.length && goal[idx].equals(cards1[idx1])){
                idx++;
                idx1++;
            }
            else if(idx2 < cards2.length && goal[idx].equals(cards2[idx2])){
                idx++;
                idx2++;
            }
            else{
                answer = "No";
                break;
            }
        }
        return answer;
    }
}