import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] inorderArr;
    static int[] postorderArr;
    static int[] preroderArr;
    static int idx = 0;

    public static void main(String[] args) throws IOException {
        init();
        preorder(0, n, 0, n);
        //System.out.println(Arrays.toString(preroderArr));
        StringBuilder sb = new StringBuilder();
        for (int node : preroderArr) {
            sb.append(node).append(" ");
        }
        System.out.println(sb.toString());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        inorderArr = new int[n];
        postorderArr = new int[n];
        preroderArr = new int[n];
        for (int i = 0; i < n; i++) {
            inorderArr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            postorderArr[i] = Integer.parseInt(st.nextToken());
        }
    }

    static void preorder(int inStart, int inEnd, int postStart, int postEnd) {
        //System.out.println(" " + inStart + " " + inEnd + " " + postStart + " " + postEnd);
        StringBuilder result = new StringBuilder();
        int value = postorderArr[postEnd - 1];
        int rootIdx = 0;
        for (int i = inStart; i < inEnd; i++) {
            if (inorderArr[i] == value) {
                rootIdx = i;
            }
        }
        preroderArr[idx] = value;
        if (rootIdx - inStart >= 1) {
            idx += 1;
            preorder(inStart, rootIdx, postStart, postStart + (rootIdx - inStart));
        }
        if (inEnd - (rootIdx + 1) >= 1) {
            idx += 1;
            preorder(rootIdx + 1, inEnd, postStart + (rootIdx - inStart), postEnd - 1);
        }
    }

}
