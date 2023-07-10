import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static int n;
    public static int[] arr;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(solution());
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n + 1];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[i] = y;
        }
        arr[n] = 0;
    }

    public static int solution() {
        int result = 0;
        Stack<Integer> stack = new Stack<>();
        for (int h : arr) {
//            System.out.println(stack);
//            System.out.println(result);
            if (stack.isEmpty() || stack.peek() < h) {
                stack.push(h);
            }else{
                while((!stack.isEmpty()) && stack.peek() > h) {
                    stack.pop();
                    result++;
                }
                if ((stack.isEmpty()) || stack.peek() < h) stack.push(h);
            }
        }
        return result;
    }
}
