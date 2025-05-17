import java.util.*;

class Solution {
    private static final int base = 26;
    
    public String solution(long n, String[] bans) {
        String answer = "";
        long[] banNums = new long[bans.length];
        for (int i = 0; i < bans.length; i++) {
            banNums[i] = order(bans[i]);
        }
        Arrays.sort(banNums);
        for (long banNum : banNums) {
            if (n < banNum) {
                return spell(n);
            }
            n++;
        }
        return spell(n);
    }
    
    private long order (String spell) {
        long result = 0;
        for (int i = 0; i < spell.length(); i++) {
            char alphabet = spell.charAt(i);
            int placeValue = num(alphabet);
            long value = placeValue * (long) Math.pow(base, spell.length() - i - 1);
            result += value;
        }
        return result;
    }
    
    private String spell (long order) {
        StringBuilder sb = new StringBuilder();
        boolean curFlag = false;
        boolean nxtFlag = false;
        while (order != 0) {
            int mod = (int)(order % base);
            if (mod == 0) {
                nxtFlag = true;
                mod = base;
            }
            if (curFlag) mod--;
            if (mod == 0) {
                if (order / base == 0) {
                    break;
                }
                nxtFlag = true;
                mod = base;
            }
            sb.append(alphabet(mod));
            order /= base;
            curFlag = nxtFlag;
            nxtFlag = false;
        }
        return sb.reverse().toString();
    }
    
    private int num (char alphabet) {
        return (int)alphabet - 96;
    }
    
    private char alphabet (int order) {
        return (char) (order + 96);
    }
}