import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class Main {
    public static List<Character> vowels = List.of('a', 'e', 'i', 'o', 'u');

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String password = br.readLine();
            if (password.equals("end")) return;
            if (isAcceptable(password)) {
                System.out.printf("<%s> is acceptable.\n", password);
            } else {
                System.out.printf("<%s> is not acceptable.\n", password);
            }
        }
    }
    
    public static boolean isAcceptable(String password) {
        if (!containVowel(password)) return false;
        if (continuousType(password)) return false;
        if (continuousCharacter(password)) return false;
        return true;
    }

    public static boolean containVowel(String password) {
        for (int i = 0; i < password.length(); i++) {
            if (isVowel(password.charAt(i))) return true;
        }
        return false;
    }

    public static boolean isVowel(char character) {
        return vowels.contains(character);
    }

    public static boolean continuousType(String password) {
        int continuousCnt = 0;
        boolean lastIsVowel = false;

        for (int i = 0; i < password.length(); i++) {
            if (isVowel(password.charAt(i))) {
                if (lastIsVowel) {
                    continuousCnt++;
                } else {
                    continuousCnt = 1;
                    lastIsVowel = true;
                }
            } else {
                if (lastIsVowel) {
                    continuousCnt = 1;
                    lastIsVowel = false;
                } else {
                    continuousCnt++;
                }
            }

            if (continuousCnt >= 3) {
                return true;
            }
        }
        return false;
    }

    public static boolean continuousCharacter(String password) {
        for (int i = 1; i < password.length(); i++) {
            if (password.charAt(i) == password.charAt(i - 1)) {
                if (password.charAt(i) != 'e' && password.charAt(i) != 'o') {
                    return true;
                }
            }
        }
        return false;
    }
}
