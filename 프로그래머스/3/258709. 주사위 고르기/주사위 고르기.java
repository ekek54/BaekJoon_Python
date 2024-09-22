/*
  1. 주사위 조합 생성
  2. A, B의 주사위 합 배열 생성
  3. A가 B상대로 몇승 가능한지 확인 - 이진 탐색
    3-1. B 합 배열 정렬
    3-2. A 합 배열 순회하며 이진탐색
    3-3. 합산
 4. 최대인 경우 반환
*/
import java.util.*;

class Solution {
    public int[] solution(int[][] dices) {
        int[] answer = {};
        int maxWins = 0;
        int n = dices.length;
        int r = n / 2;
        Combination nCr = new Combination(n, r);
        Player A = new Player();
        Player B = new Player();
        for (List<Integer> combination: nCr.getCombinations()) {
            List<int[]> aDices = new ArrayList<>();
            List<int[]> bDices = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (combination.contains(i)) {
                    aDices.add(dices[i]);
                } else {
                    bDices.add(dices[i]);
                }
            }
            A.setDices(aDices);
            B.setDices(bDices);
            int wins = cntWins(A.getSums(), B.getSums());
            if (maxWins < wins) {
                maxWins = wins;
                answer = combination.stream()
                    .mapToInt(e -> e + 1)
                    .toArray();
            }
        }
        return answer;
    }
    
    private int cntWins(List<Integer> aSums, List<Integer> bSums) {
        int result = 0;
        for (int aSum: aSums) {
            int leLastIdx = bisec(bSums, aSum);
            result += leLastIdx + 1;
        }
        return result;
    }
    
    private int bisec(List<Integer> nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums.get(mid) < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return r;
    }
        
}

class Combination {
    private int n, r;
    private List<List<Integer>> combinations;
    private Stack<Integer> stack = new Stack<>();
    
    public Combination(int n, int r) {
        this.n = n;
        this.r = r;
        this.combinations = new ArrayList<>();
        dfs(0);
    }
    
    private void dfs(int cnt) {
        if (cnt == r) {
            combinations.add(new ArrayList<>(stack));
            return;
        }
        
        for (int i = 0; i < n; i++) {
            if (!stack.isEmpty() && stack.peek() >= i) {
                continue;
            }
            
            stack.add(i);
            dfs(cnt + 1);
            stack.pop();
        }
    }
    
    public List<List<Integer>> getCombinations() {
        return combinations;
    }
}

class Player {
    private List<int[]> dices = new ArrayList<>();
    private int sum = 0;
    
    public Player() {}
    
    public void setDices(List<int[]> dices) {
        this.dices = dices;
    }
    
    public List<Integer> getSums() {
        List<Integer> sums = new ArrayList<>(); 
        dfs(0, sums);
        sums.sort(Integer::compareTo);
        return sums;
    }
    
    private void dfs(int cnt, List<Integer> sums) {
        if (cnt == dices.size()) {
            sums.add(sum);
            return;
        }
        
        for (int i = 0; i < 6; i++) {
            sum += dices.get(cnt)[i];
            dfs(cnt + 1, sums);
            sum -= dices.get(cnt)[i];
        }
    }
}