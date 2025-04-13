class Solution {
    public int solution(int a, int b) {
        int A = concatInt(a, b);
        int B = concatInt(b, a);
        return A >= B ? A : B;
    }
    
    private int concatInt(int a, int b) {
        return Integer.parseInt(Integer.toString(a) + Integer.toString(b));
    }
}