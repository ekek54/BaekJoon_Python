import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int L, C;
    static char[] alphas;
    static List<String> answer = new ArrayList<>();
    static Stack<Integer> stack = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        alphas = new char[C];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            alphas[i] = st.nextToken().charAt(0);
        }
        Arrays.sort(alphas);
//        System.out.println("alphas = " + Arrays.toString(alphas));
        dfs(0);
        for (String s : answer) {
            System.out.println(s);
        }
    }

    public static void dfs(int cnt) {
        if (cnt == L) {
            String s = buildString();
            if (hasOneVowelAndTwoConsonant(s)) answer.add(s);
            return;
        }

        for (int i = 0; i < C; i++) {
            if (!stack.isEmpty() && stack.peek() >= i) continue;
            stack.push(i);
            dfs(cnt + 1);
            stack.pop();
        }
    }

    private static boolean hasOneVowelAndTwoConsonant(String s) {
        char[] vowels = new char[] {'a', 'e', 'i', 'o', 'u'};
        int vowelCnt = 0;
        for (int i = 0; i < L; i++) {
            for (int j = 0; j < vowels.length; j++) {
                if (s.charAt(i) == vowels[j]) vowelCnt++;
            }
        }
        int consonantCnt = s.length() - vowelCnt;
        return vowelCnt >= 1 && consonantCnt >= 2;
    }

    public static String buildString() {
        StringBuilder sb = new StringBuilder();
        for (Integer idx : stack) {
            sb.append(alphas[idx]);
        }
        return sb.toString();
    }
}
