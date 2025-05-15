import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> pokemons = new HashSet<>();
        for (int num : nums) {
            pokemons.add(num);
        }
        System.out.println(pokemons);
        int N = nums.length;
        return Math.min(N / 2, pokemons.size());
    }
}