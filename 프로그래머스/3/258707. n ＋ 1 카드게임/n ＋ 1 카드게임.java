import java.util.*;

class Solution {
    public int solution(int coin, int[] cards) {
        int N = cards.length;
        Card[] cardsInOrder = new Card[N];
        int maxRound = N / 3;
        for (int i = 0; i < N / 2; i++) {
            Card card1 = new Card();
            Card card2 = new Card();
            card1.setCouple(card2);
            card2.setCouple(card1);
            
            cardsInOrder[i] = card1;
            cardsInOrder[N - 1 - i] = card2;
        }
        
        for (int i = 0; i < N; i++) {
            int idx = cards[i] - 1;
            if (i < N / 3) {
                cardsInOrder[idx].setRound(0);
                continue;
            }
            cardsInOrder[idx].setRound((i - N / 3) / 2 + 1);
        }
        
        int round = 1;
        while (round <= maxRound) {
            int minReqCoin = 3;
            Card greedyCard = null;
            
            for (int i = 0; i < N / 3 + round * 2; i++) {
                int curCardIdx = cards[i] - 1;
                Card curCard = cardsInOrder[curCardIdx];
                Card coupleCard = curCard.couple;
                if (curCard.isUsed) continue;
                if (coupleCard.round > round) continue;
                
                int reqCoin = 0;
                if (curCard.round > 0) reqCoin++;
                if (coupleCard.round > 0) reqCoin++;
                
                if (minReqCoin > reqCoin) {
                    minReqCoin = reqCoin;
                    greedyCard = curCard;
                }
            }
            
            if (greedyCard == null) break;
            if (coin < minReqCoin) break;
            greedyCard.use();
            greedyCard.couple.use();
            coin -= minReqCoin;
            round++;
        }
        return round;
    }
    
    
}

class Card {
    public Card couple;
    public int round;
    public boolean isUsed = false;
    
    public Card() {
    }
    
    public void setCouple(Card couple) {
        this.couple = couple;
    }
    
    public void setRound(int round) {
        this.round = round;
    }
    
    public void use() {
        this.isUsed = true;
    }
    
    @Override
    public String toString() {
        return "" + round + "," + isUsed;
    }
}