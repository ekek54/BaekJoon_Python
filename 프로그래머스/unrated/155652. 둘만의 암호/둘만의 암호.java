class Solution {
    public String solution(String s, String skip, int index) {
        String alpha = "abcdefghijklmnopqrstuvwxyz";
        StringBuilder skippedAlpha = new StringBuilder();
        StringBuilder answerSB = new StringBuilder();
        for(int i = 0; i < 26; i ++){
            if (!skip.contains(alpha.substring(i,i + 1))){
                skippedAlpha.append(alpha.charAt(i));
            }
        }
        for(int i = 0; i < s.length(); i++){
            int convIdx = (skippedAlpha.indexOf(s.substring(i, i+1)) + index) % skippedAlpha.length();
            answerSB.append(skippedAlpha.substring(convIdx, convIdx + 1));
        }
        //System.out.println(skippedAlpha.toString());
        String answer = answerSB.toString();
        return answer;
    }
}