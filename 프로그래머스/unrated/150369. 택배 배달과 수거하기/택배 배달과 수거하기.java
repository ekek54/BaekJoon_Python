// 최단거리 이동을 위해서 가장 멀리 있는 일들을 먼저 처리해야한다.


class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        int d;
        int p;
        for (d = n - 1; d >= 0; d --){
            if(deliveries[d] != 0) break;
        }
        for (p = n - 1; p >= 0; p --){
            if(pickups[p] != 0) break;
        }
        while (d >= 0 || p >= 0){
            int inven = cap;
            answer += 2 * (Math.max(d, p) + 1);
            while (inven >= 0 && d >= 0){
                if (deliveries[d] > inven){
                    deliveries[d] -= inven;
                    break;
                }
                else{
                    inven -= deliveries[d];
                    deliveries[d] = 0;
                    d -= 1;
                }
            }
            inven = cap;
            while (inven >= 0 && p >= 0){
                if (pickups[p] > inven){
                    pickups[p] -= inven;
                    break;
                }
                else{
                    inven -= pickups[p];
                    pickups[p] = 0;
                    p -= 1;
                }
            }
        }
        return answer;
    }
}