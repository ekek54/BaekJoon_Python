class Solution {
    public int solution(int a, int b) {
        int A = concatInt(a, b);
        int B = 2 * a * b;
        return A >= B ? A : B;
    }
    
    private int concatInt(int a, int b) {
        return Integer.parseInt(Integer.toString(a) + Integer.toString(b));
    }
}