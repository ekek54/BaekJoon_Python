import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final char[] DNA_CODES = new char[] {'A', 'C', 'G', 'T'};
    private static Map<Character, Integer> requires = new HashMap<>();

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        String DNA = br.readLine();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < DNA_CODES.length; i++) {
            requires.put(DNA_CODES[i], Integer.parseInt(st.nextToken()));
        }
        Map<Character, Integer> window = new HashMap<>();
        for (int i = 0; i < DNA_CODES.length; i++) {
            window.put(DNA_CODES[i], 0);
        }
        for (int i = 0; i < P; i++) {
            char code = DNA.charAt(i);
            window.put(code, window.get(code) + 1);
        }
        int answer = 0;
        if (isSafe(window)) {
            answer += 1;
        }

        for (int i = 0; i < DNA.length() - P; i++) {
            char outcode = DNA.charAt(i);
            char incode = DNA.charAt(i + P);
            window.put(outcode, window.get(outcode) - 1);
            window.put(incode, window.get(incode) + 1);
            if (isSafe(window)) answer += 1;
        }

        System.out.println(answer);
    }

    private static boolean isSafe(Map<Character, Integer> window) {
        for (Character code : window.keySet()) {
            if (window.get(code) < requires.get(code)) {
                return false;
            }
        }
        return true;
    }
}
