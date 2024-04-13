class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int requireTime = bandage[0];
        int healPerSec = bandage[1];
        int bonusHeal = bandage[2];
        int lastAttackAt = 0;
        int maxHealth = health;
        for (int[] attack: attacks) {
            int attackAt = attack[0];
            int attackDamage = attack[1];
            //회복 적용
            int term = attackAt - lastAttackAt - 1;
            int doneCnt = term / requireTime;
            int healSum = term * healPerSec + doneCnt * bonusHeal;
            health = Math.min(maxHealth, health + healSum);
            // System.out.println(" " + term + " "+doneCnt + " " + healSum + " " + health);
            //공격 적용
            health -= attackDamage;
            lastAttackAt = attackAt;
            // System.out.println(health);
            if (health <= 0) return -1;
        }
        
        return health;
    }
}