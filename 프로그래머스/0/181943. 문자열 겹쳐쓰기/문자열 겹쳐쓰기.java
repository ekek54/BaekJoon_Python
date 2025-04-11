class Solution {
    public String solution(String myString, String overwriteString, int s) {
        return myString.substring(0, s) + overwriteString + myString.substring(s + overwriteString.length());
    }
}