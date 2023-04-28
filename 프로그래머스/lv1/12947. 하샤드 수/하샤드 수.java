class Solution {
    public boolean solution(int x) {
        int sumOfDigits = 0;
        int tmp_x = x;
        while(tmp_x > 0) {
            sumOfDigits += tmp_x % 10;
            tmp_x /=10;
        }
        if (x % sumOfDigits == 0) {
            return true;
        }
        return false;
    }
}