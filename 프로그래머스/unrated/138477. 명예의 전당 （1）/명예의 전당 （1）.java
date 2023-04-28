import java.util.*;
class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < score.length; i++){
            //System.out.println(Arrays.toString(pq.toArray()));
            if(pq.size() < k){
                pq.add(score[i]);
            }
            else if(score[i] > pq.peek()){
                pq.poll();
                pq.add(score[i]);
            }
            answer[i] = pq.peek();
        }
        return answer;
    }
}