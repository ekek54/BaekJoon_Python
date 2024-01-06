import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static int N;
    public static Map<String, Integer> nameToIdx = new HashMap<>();
    public static Node[] nodes;
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        init();
//        System.out.println(nameToIdx);
//        System.out.println(Arrays.toString(nodes));
        printPreorder();
        printInorder();
        printPostorder();
    }

    private static void init() throws IOException {
        nodes = new Node[N];
        char A = 'A';
        for (int i = 0; i < N; i++) {
            String nodeName = Character.toString(A + i);
            nodes[i] = new Node(nodeName);
            nameToIdx.put(nodeName, i);
        }

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String curName = st.nextToken();
            String leftName = st.nextToken();
            if (!leftName.equals(".")) {
                nodes[nameToIdx.get(curName)].left = nameToIdx.get(leftName);
            }
            String rightName = st.nextToken();
            if (!rightName.equals(".")) {
                nodes[nameToIdx.get(curName)].right = nameToIdx.get(rightName);
            }
        }
    }

    private static void printPreorder() {
        StringBuilder orderBuilder = new StringBuilder();
        preorder(nodes[0], orderBuilder);
        System.out.println(orderBuilder);
    }

    private static void preorder(Node node, StringBuilder orderBuilder) {
        orderBuilder.append(node.Name);
        if (node.left != -1) {
            preorder(nodes[node.left], orderBuilder);
        }
        if (node.right != -1) {
            preorder(nodes[node.right], orderBuilder);
        }
    }

    private static void printInorder() {
        StringBuilder orderBuilder = new StringBuilder();
        inorder(nodes[0], orderBuilder);
        System.out.println(orderBuilder);
    }

    private static void inorder(Node node, StringBuilder orderBuilder) {
        if (node.left != -1) {
            inorder(nodes[node.left], orderBuilder);
        }
        orderBuilder.append(node.Name);
        if (node.right != -1) {
            inorder(nodes[node.right], orderBuilder);
        }
    }

    private static void printPostorder() {
        StringBuilder orderBuilder = new StringBuilder();
        postorder(nodes[0], orderBuilder);
        System.out.println(orderBuilder);
    }

    private static void postorder(Node node, StringBuilder orderBuilder) {
        if (node.left != -1) {
            postorder(nodes[node.left], orderBuilder);
        }
        if (node.right != -1) {
            postorder(nodes[node.right], orderBuilder);
        }
        orderBuilder.append(node.Name);
    }
    static class Node {
        String Name;
        int left = -1;
        int right = -1;

        public Node(String name) {
            Name = name;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "Name='" + Name + '\'' +
                    ", left=" + left +
                    ", right=" + right +
                    '}';
        }
    }
}