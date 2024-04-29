import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < works.length; i++) {
            pq.add(works[i]);
        }
        for (int i = 0; i < n; i++) {
            if (pq.peek() == 0) break;
            pq.add(pq.poll() - 1);
        }
        long answer = 0;
        for(Integer work: pq) {
            answer += Math.pow(work, 2);
        }
        System.out.println(pq);
        return answer;
    }
}