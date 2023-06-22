import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while ((input = br.readLine()) != null) {
            Trie trie = new Trie();
            N = Integer.parseInt(input);
            for (int i = 0; i < N; i++) {
                String word = br.readLine().strip();
                trie.insertWord(word);
            }
            System.out.printf("%.2f%n",trie.average());
        }
    }

    static class Trie {
        private final Node root = new Node('#');

        public void insertWord(String word) {
            Node cur = root;
            for (int i = 0; i < word.length(); i++) {
                if (i == word.length() - 1) {
                    if (cur.contain(word.charAt(i))) {
                        cur = cur.findAtChild(word.charAt(i));
                    } else {
                        Node newNode = new Node(word.charAt(i));
//                        System.out.println(word.charAt(i));
                        cur.getChildren().add(newNode);
                        cur = newNode;
                    }
                } else {
                    if (cur.contain(word.charAt(i))) {
                        cur = cur.findAtChild(word.charAt(i));
                    } else {
                        Node newNode = new Node(word.charAt(i));
                        cur.getChildren().add(newNode);
//                        System.out.println(word.charAt(i));
                        cur = newNode;
                    }
                }
            }
            Node endNode = new Node('.');
            cur.getChildren().add(endNode);
        }

        public double average() {
            int sum = typeSum(root, 0, 0);
//            System.out.println("sum = " + sum);
            return (double) sum / N;
        }

        public int typeSum(Node node, int typeCount, int sum) {
//            System.out.println("node = " + node);
//            System.out.println("typeCount = " + typeCount);
//            System.out.println("sum = " + sum);
            if (node.getChildren().size() == 0) {
                sum += typeCount;
                return sum;
            }
            if (node.getCharacter() !='#' && node.getChildren().size() == 1) {
                sum = typeSum(node.getChildren().get(0), typeCount, sum);
                return sum;
            }
            for (Node child : node.getChildren()) {
                if (child.getCharacter() == '.') {
                    sum = typeSum(child, typeCount, sum);
                }else {
                    sum = typeSum(child, typeCount + 1, sum);
                }
            }
            return sum;
        }
    }

    static class Node {
        private final char character;
        private final ArrayList<Node> children = new ArrayList<>();

        public Node(char character) {
            this.character = character;
        }

        public boolean contain(char a) {
            for (Node child : children) {
                if (child.getCharacter() == a) return true;
            }
            return false;
        }

        public Node findAtChild(char a) {
            for (Node child : children) {
                if (child.getCharacter() == a) return child;
            }
            throw new IllegalStateException();
        }

        public char getCharacter() {
            return character;
        }

        public ArrayList<Node> getChildren() {
            return children;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "character=" + character +
                    '}';
        }
    }
}
