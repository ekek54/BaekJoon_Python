import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        init();
        StringBuilder sb = new StringBuilder();
        for (Integer e : solution()) {
            sb.append(e).append(" ");
        }
        System.out.println(sb.toString());
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }

    public static ArrayList<Integer> solution() {
        Stack<Element> stack = new Stack<>();
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            while (!stack.isEmpty()) {
                if (stack.peek().value < arr[i]) {
                    stack.pop();
                }else break;
            }
            if (stack.isEmpty()) {
                result.add(0);
            }else {
                result.add(stack.peek().idx);
            }
            stack.add(new Element(arr[i], i + 1));
        }
        return result;
    }
    static class Element {
        public int value;
        public int idx;

        public Element(int value, int idx) {
            this.value = value;
            this.idx = idx;
        }
    }
}