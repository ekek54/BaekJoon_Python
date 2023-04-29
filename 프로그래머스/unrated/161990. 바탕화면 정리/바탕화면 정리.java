class Solution {
    public int[] solution(String[] wallpaper) {
        int N = wallpaper.length;
        int M = wallpaper[0].length();
        int minR = N;
        int minC = M;
        int maxR = 0;
        int maxC = 0;
        for(int i = 0; i < N; i ++){
            for(int j = 0; j < M; j ++){
                if(wallpaper[i].charAt(j) == '#'){
                    minR = Math.min(minR, i);
                    minC = Math.min(minC, j);
                    maxR = Math.max(maxR, i);
                    maxC = Math.max(maxC, j);
                }
            }
        }
        int[] answer = {minR, minC, maxR + 1, maxC + 1};
        return answer;
    }
}