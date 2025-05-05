class Solution {
    public int[] solution(int brown, int yellow) {
        int area = brown + yellow;
        for (int w = area; w > 2; w--) {
            if (area % w != 0) continue;
            int h = area / w;
            if (h <= 2) continue;
            int yellowW = w - 2;
            int yellowH = h - 2;
            if (yellowW * yellowH == yellow) {
                return new int[] {w, h};
            }
            
        }
        return new int[] {0, 0};
    }
}