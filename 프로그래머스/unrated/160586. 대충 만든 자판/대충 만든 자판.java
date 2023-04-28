import java.util.*;
class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        HashMap<Character, Integer> map= new HashMap<>();
        for(int i = 0; i < keymap.length; i ++){
            for(int j = 0; j < keymap[i].length(); j++){
                char curChar = keymap[i].charAt(j);
                if (!map.containsKey(curChar) || map.containsKey(curChar) && map.get(curChar) > j + 1){
                    map.put(curChar, j + 1);
                }
            }
        }
        for(int i = 0; i < targets.length; i ++){
            for(int j = 0; j < targets[i].length(); j ++){
                if (!map.containsKey(targets[i].charAt(j))){
                    answer[i] = -1;
                    break;
                }
                else{
                    answer[i] += map.get(targets[i].charAt(j));
                }
            }
        }
        //System.out.println(map);
        return answer;
    }
}