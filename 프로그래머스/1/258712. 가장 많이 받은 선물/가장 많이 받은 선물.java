import java.util.*;

class Solution {
    private String[] friends;
    private String[] gifts; 
    private int N;
    private Map<String, Integer> idxOfFriend;
    private int[] giftScores;
    private int[][] giftBoard;
    private int[] pRecvCnts;
    
    public Integer solution(String[] friends, String[] gifts) {
        //init
        this.friends = friends;
        this.gifts = gifts;
        N = friends.length;
        idxOfFriend = initIdxOfFriend();
        giftScores = new int[N];
        giftBoard = initGiftBoard();
        pRecvCnts = new int[N];
        
        //logic
        calcGiftScore();
        predictRecvCnt();
        
        int answer = 0;
        return Arrays.stream(pRecvCnts).max().orElse(0);
    }
    
    private void predictNextGift() {
        
    }
    
    private void predictRecvCnt() {
        for (int i = 0; i < N; i++) {
            int pRecvCnt = 0;
            for (int j = 0; j < N; j++) {
                if (giftBoard[i][j] > giftBoard[j][i]) {
                    pRecvCnt += 1;
                    continue;
                }
                if (giftBoard[i][j] == giftBoard[j][i] && giftScores[i] > giftScores[j]) {
                    pRecvCnt += 1;
                    continue;
                }
            }
            pRecvCnts[i] = pRecvCnt;
        }
    }
    
    private void calcGiftScore() {
        for (int i = 0; i < N; i++) {
            int sendCnt = 0;
            int recvCnt = 0;
            for (int j = 0; j < N; j++) {
                sendCnt += giftBoard[i][j];
                recvCnt += giftBoard[j][i];
            }
            int giftScore = sendCnt - recvCnt;
            giftScores[i] = giftScore;
        }
    }
    
    private int[][] initGiftBoard() {
        int[][] giftBoard = new int[N][N];
        for (String gift: gifts) {
            StringTokenizer st = new StringTokenizer(gift);
            String from = st.nextToken();
            String to = st.nextToken();
            giftBoard[idxOfFriend.get(from)][idxOfFriend.get(to)] += 1;
        }
        return giftBoard;
    }
    
    private Map<String, Integer> initIdxOfFriend() {
        Map<String, Integer> res = new HashMap<>();
        int i = 0;
        for (String name: friends) {
            res.put(name, i++);
        }
        return res;
    }
}