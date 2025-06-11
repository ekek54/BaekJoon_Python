import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        String formular = br.readLine();
        boolean meetMinus = false;
        StringBuilder sb = new StringBuilder();
        int answer = 0;
        for (int i = 0; i < formular.length(); i++) {
            if (formular.charAt(i) == '+' || formular.charAt(i) == '-') {
                if (meetMinus) {
                    answer -= Integer.parseInt(sb.toString());
                } else {
                    answer += Integer.parseInt(sb.toString());
                }
                sb = new StringBuilder();
                if (formular.charAt(i) == '-') {
                    meetMinus = true;
                }
            }else {
                sb.append(formular.charAt(i));
            }
        }
        if (meetMinus) {
            answer -= Integer.parseInt(sb.toString());
        } else {
            answer += Integer.parseInt(sb.toString());
        }
        System.out.println(answer);
    }
}