import java.util.ArrayList;

class Solution {
    public ArrayList<String> solution(String my_str, int n) {
        ArrayList<String> answer = new ArrayList<String>();
        for(int i = 0; i < my_str.length(); i += n){
            int end = i + n;
            if(end > my_str.length()){
                end = my_str.length();
            }
            answer.add(my_str.substring(i,end));
        }
        return answer;
    }
}