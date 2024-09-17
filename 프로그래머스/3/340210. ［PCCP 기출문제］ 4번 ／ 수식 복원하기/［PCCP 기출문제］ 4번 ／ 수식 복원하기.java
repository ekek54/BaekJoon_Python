import java.util.*;

class Solution {
    public String[] solution(String[] expressions) {
        Set<Integer> possibleRadixes = new HashSet<>(Arrays.asList(2, 3, 4, 5, 6, 7, 8, 9));
        
        List<Expression> allExpressions = new ArrayList<>();
        List<Expression> blankExpressions = new ArrayList<>();
        for (String expression: expressions) {
            Expression e = new Expression(expression);
            allExpressions.add(e);
            if (e.solutionIsBlank()) {
                blankExpressions.add(e);
            }
        }
        for (Expression expression: allExpressions) {
            possibleRadixes.retainAll(expression.possibleRadixes());
        }
        
        String[] answer = new String[blankExpressions.size()];
        for (int i = 0; i < blankExpressions.size(); i++) {
            answer[i] = blankExpressions.get(i).completeExpression(possibleRadixes);
        }
        return answer;
    }
}

class Expression {
    public String expressionString;
    public String A, B;
    public String solution;
    public String operator;
    
    public Expression (String expression) {
        this.expressionString = expression;
        StringTokenizer st = new StringTokenizer(expression);
        this.A = st.nextToken();
        this.operator = st.nextToken();
        this.B = st.nextToken();
        st.nextToken(); //"=" skip
        this.solution = st.nextToken();
    }
    
    public boolean solutionIsBlank() {
        return solution.equals("X");
    }
    
    public Set<Integer> possibleRadixes() {
        Set<Integer> result = new HashSet<>();
        for (int i = 2; i <= 9; i++) {
            if (isSolvedAs(i)) {
                result.add(i);
            }
        } 
        return result;
    }
    
    private boolean isSolvedAs(int radix) {
        try {
            if (!solutionIsBlank()) {
                int decimalA = Integer.parseInt(A, radix);
                int decimalB = Integer.parseInt(B, radix);
                if (operator.equals("+")) {
                    return decimalA + decimalB == Integer.parseInt(solution, radix);
                } 
                else {
                    return decimalA - decimalB == Integer.parseInt(solution, radix);
                }
            } else {
                int decimalA = Integer.parseInt(A, radix);
                int decimalB = Integer.parseInt(B, radix);
                return true;
            }
        } catch(NumberFormatException e) { 
            // radix를 벗어나는 수로 인해 진법 변환 오류 발생시 불가
            return false;
        }
    }
    
    public String completeExpression(Set<Integer> radixes) {
        if (!solutionIsBlank()) {
            return expressionString;
        }
        List<String> answers = new ArrayList<>();
        for (int radix: radixes) {
            answers.add(solveAs(radix));
        }
        Set answerSet = new HashSet<String>(answers);
        if (answerSet.size() == 1) {
            return expressionString.replace("X", answers.get(0));
        } else {
            return expressionString.replace("X", "?");
        }
    }
    
    private String solveAs(int radix) {
        int decimalA = Integer.parseInt(A, radix);
        int decimalB = Integer.parseInt(B, radix);
        if (operator.equals("+")) {
            return Integer.toString(decimalA + decimalB, radix);
        } 
        else {
            return Integer.toString(decimalA - decimalB, radix);
        }
    }
}