import java.util.*;

class Solution {
    public String solution(String myString, int k) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            sb.append(myString);
        }
        return sb.toString();
    }
}