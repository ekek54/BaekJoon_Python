import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        HashMap<String, Integer> playerIdx = new HashMap<>();
        for(int i = 0; i < players.length; i ++){
            playerIdx.put(players[i], i);
        }
        for(int i = 0; i < callings.length; i ++){
            String curPlayer = callings[i];
            int curIdx = playerIdx.get(curPlayer);
            String prePlayer = players[curIdx - 1];
            playerIdx.put(curPlayer, curIdx - 1);
            playerIdx.put(prePlayer, curIdx);
            String tmp = players[curIdx];
            players[curIdx] = players[curIdx - 1];
            players[curIdx - 1] = tmp;
        }
        return players;
    }
}