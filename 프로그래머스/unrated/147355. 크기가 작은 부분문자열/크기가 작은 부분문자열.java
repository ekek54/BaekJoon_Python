class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        long longP = Long.parseLong(p);
        for(int i = 0; i < t.length() - p.length() + 1; i++){
            String subStr = t.substring(i, i + p.length());
            long longSubStr = Long.parseLong(subStr);
            if (longP >= longSubStr){
                answer += 1;
            }
            //System.out.println(subStr);
        }
        return answer;
    }
}