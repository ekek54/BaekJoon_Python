import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Stack<Integer> stack = new Stack<>();

        int targetIdx = 0;
        List<Character> logs = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            stack.add(i);
            logs.add('+');
            while (!stack.isEmpty() && stack.peek() == arr[targetIdx]) {
                stack.pop();
                logs.add('-');
                targetIdx++;
            }
//            System.out.println(stack);
        }

        if (!stack.isEmpty()) {
            System.out.println("NO");
            return;
        }

        for (char log : logs) {
            System.out.println(log);
        }
    }
}
