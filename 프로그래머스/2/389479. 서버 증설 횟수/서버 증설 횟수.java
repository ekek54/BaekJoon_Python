import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        Queue<Integer> serverQue = new LinkedList<>(); // 시작 시간 담기
        for (int i = 0; i < 24; i++) {
            while(!serverQue.isEmpty() && serverQue.peek() + k <= i) {
                serverQue.poll();
            }
            int player = players[i];
            int requireServerCnt = player / m;
            while (requireServerCnt > serverQue.size()) {
                serverQue.add(i);
                answer++;
            }
        }
        
        return answer;
    }
    
    
}