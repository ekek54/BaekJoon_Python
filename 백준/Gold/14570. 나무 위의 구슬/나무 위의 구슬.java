import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Optional;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static Node[] nodes;
    static long K;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(solution());
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            nodes[i] = new Node(i + 1);
        }
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            Node curNode = nodes[i];
            int U = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            if (U != -1) curNode.setLeft(nodes[U - 1]);
            if (V != -1) curNode.setRight(nodes[V - 1]);
        }
        st = new StringTokenizer(br.readLine());
        K = Long.parseLong((st.nextToken()));
    }

    static public int solution() {
        Node curNode = nodes[0];
        while (!curNode.isLeaf()) {
//            System.out.println("curNode = " + curNode.getNum());
            if (curNode.hasTwin()) {
                if (K % 2 == 0) {
                    K /= 2;
                    curNode = curNode.getRight().orElseThrow();
                } else {
                    K = K / 2 + 1;
                    curNode = curNode.getLeft().orElseThrow();
                }
            } else if (curNode.hasLeft()) {
                curNode = curNode.getLeft().orElseThrow();
            } else {
                curNode = curNode.getRight().orElseThrow();
            }
        }
        return curNode.getNum();
    }

    static class Node {
        private final int num;
        private Optional<Node> left = Optional.empty();
        private Optional<Node> right = Optional.empty();

        public int getNum() {
            return num;
        }
        public Node(int num) {
            this.num = num;
        }

        public Optional<Node> getLeft() {
            return left;
        }

        public void setLeft(Node left) {
            this.left = Optional.ofNullable(left);
        }

        public Optional<Node> getRight() {
            return right;
        }

        public void setRight(Node right) {
            this.right = Optional.ofNullable(right);
        }

        public boolean isLeaf() {
            return left.isEmpty() && right.isEmpty();
        }

        public boolean hasLeft() {
            return left.isPresent();
        }

        public boolean hasRight() {
            return right.isPresent();
        }

        public boolean hasTwin() {
            return hasLeft() && hasRight();
        }
    }


}
