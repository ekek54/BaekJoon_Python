import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static final String targetRegx = "^((100+1+)|01)+$";

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputString = br.readLine().strip();
        System.out.println(answerFormat(match(inputString)));
    }

    static public boolean match(String inputString) {
        return inputString.matches(targetRegx);
    }

    static public String answerFormat(boolean match) {
        return match ? "SUBMARINE" : "NOISE";
    }
}
