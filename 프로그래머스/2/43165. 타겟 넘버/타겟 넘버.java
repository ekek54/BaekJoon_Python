class Solution {
    private int[] numbers;
    private int target;
    private int answer = 0;
    private int cur = 0;
    
    public int solution(int[] numbers, int target) {
        this.numbers = numbers;
        this.target = target;
        dfs(0);
        return answer;
    }
    
    private void dfs(int cnt) {
        if (cnt == numbers.length) {
            if (cur == target) {
                answer += 1;
            }
            return;
        }
        
        // 더하는 경우
        cur += numbers[cnt];
        dfs(cnt + 1);
        cur -= numbers[cnt];
        
        // 빼는 경우
        cur -= numbers[cnt];
        dfs(cnt + 1);
        cur += numbers[cnt];
    }
}