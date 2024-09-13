class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        return bisectLeft(diffs, times, limit);
    }
    
    public long calculateTime(int level, int[] diffs, int[] times) {
        int n = diffs.length;
        long total = 0;
        for (int i = 0; i < n; i++) {
            int failCnt = diffs[i] <= level ? 0 : diffs[i] - level;
            int curTime = 0;
            if (failCnt > 0) {
                curTime = (times[i - 1] + times[i]) * failCnt + times[i];
            } else {
                curTime = times[i];
            }
            total += curTime;
        }
        return total;
    }
    
    public int bisectLeft(int[] diffs, int[] times, long limit) {
        int left = 1;
        int right = 300000;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (calculateTime(mid, diffs, times) <= limit) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}