import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int T;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            System.out.println(solution());
        }
    }

    public static DualPriorityQueue solution() throws IOException {
        int k = Integer.parseInt(br.readLine());
        DualPriorityQueue dpq = new DualPriorityQueue();
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            char operator = st.nextToken().charAt(0);
            int operand = Integer.parseInt(st.nextToken());
            dpq.operation(operator, operand);
        }
        return dpq;
    }

    static class DualPriorityQueue {
        private final PriorityQueue<Integer> minPQ = new PriorityQueue<>();
        private final PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Collections.reverseOrder());
        private final Map<Integer, Integer> numMap = new HashMap<>();

        private int size = 0;

        public void operation(char operator, int operand) {
            switch (operator) {
                case 'I' : 
                    insert(operand);
                    break;
                case 'D' :
                    delete(operand);
                    break;
                default:
                    throw new IllegalStateException("Unexpected value: " + operator);
            }
        }

        public void insert(int num) {
            size++;
            minPQ.add(num);
            maxPQ.add(num);
            if (numMap.containsKey(num)) {
                numMap.put(num, numMap.get(num) + 1);
            } else {
                numMap.put(num, 1);
            }
        }

        public void delete(int type) {
            if (size == 0) return;
            size--;
            if (type == 1) {
                deleteMax();
            } else if (type == -1) {
                deleteMin();
            }
        }

        public void deleteMin() {
            while (!minPQ.isEmpty()) {
                int pollNum = minPQ.poll();
                if (numMap.containsKey(pollNum) && numMap.get(pollNum) > 0) {
                    numMap.put(pollNum, numMap.get(pollNum) - 1);
                    break;
                }
            }
        }

        public void deleteMax() {
            while (!maxPQ.isEmpty()) {
                int pollNum = maxPQ.poll();
                if (numMap.containsKey(pollNum) && numMap.get(pollNum) > 0) {
                    numMap.put(pollNum, numMap.get(pollNum) - 1);
                    break;
                }
            }
        }

        public int minValue() {
            while (!minPQ.isEmpty()) {
                int peekNum = minPQ.peek();
                if (numMap.containsKey(peekNum) && numMap.get(peekNum) > 0) {
                    return peekNum;
                } else {
                    minPQ.poll();
                }
            }
            throw new IllegalStateException();
        }

        public int maxValue() {
            while (!maxPQ.isEmpty()) {
                int peekNum = maxPQ.peek();
                if (numMap.containsKey(peekNum) && numMap.get(peekNum) > 0) {
                    return peekNum;
                } else {
                    maxPQ.poll();
                }
            }
            throw new IllegalStateException();
        }

        public int getSize() {
            return size;
        }

        @Override
        public String toString() {
            return size == 0? "EMPTY": maxValue() + " " + minValue();
        }
    }
}
