import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Supoja> supojas = new ArrayList<>();
        supojas.add(new Supoja(new int[]{1, 2, 3, 4, 5}));
        supojas.add(new Supoja(new int[]{2, 1, 2, 3, 2, 4, 2, 5}));
        supojas.add(new Supoja(new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}));
        int[] scores = supojas.stream().mapToInt(s -> s.score(answers)).toArray();
        int maxScore = Arrays.stream(scores).max().getAsInt();
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < supojas.size(); i++) {
            if (scores[i] == maxScore) {
                answer.add(i + 1);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}

class Supoja {
    private int[] pattern;
    
    public Supoja(int[] pattern) {
        this.pattern = pattern;
    }
    
    public int score(int[] answers) {
        int result = 0;
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == pattern[i % pattern.length]) {
                result++;
            }
        }
        return result;
    }
}