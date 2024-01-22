import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            String input = br.readLine();
            System.out.println(palindromeType(input));
        }
    }

    private static int palindromeType(String s) {
        String remain = removeMatch(s);
        if (remain.isEmpty()) return 0;
        String removeLeft = remain.substring(1);
        String removeRight = remain.substring(0, remain.length() - 1);
        if (removeMatch(removeLeft).isEmpty() || removeMatch(removeRight).isEmpty()) return 1;
        return 2;
    }

    private static String removeMatch(String s) {
        int n = s.length();
        String remain = "";
        for (int i = 0; i < (n + 1) / 2; i++) {
            if (s.charAt(i) != s.charAt(n - 1 - i)) {
                remain = s.substring(i, n - i);
                break;
            }
        }
        return remain;
    }
}
