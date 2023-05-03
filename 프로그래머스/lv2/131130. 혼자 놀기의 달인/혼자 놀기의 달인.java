class Solution {
    public int solution(int[] cards) {
        int groupA = 0;
        int groupB = 0;
        boolean[] visit = new boolean[cards.length];
        for (int i = 0; i < cards.length; i ++){
            if (visit[i]) continue;
            int idx = i;
            int count = 0;
            while (!visit[idx]){
                count ++;
                visit[idx] = true;
                idx = cards[idx] - 1;
            }
            if (groupA < count){
                groupB = groupA;
                groupA = count;
            }
            else if(groupB < count){
                groupB = count;
            }
            
        }
        return groupA * groupB;
    }
}