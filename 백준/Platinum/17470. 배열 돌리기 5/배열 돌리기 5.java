import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N, M, R;
    static int[][] inputBoard;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        inputBoard = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                inputBoard[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        FullSquare fullSquare = new FullSquare(inputBoard);

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int op = Integer.parseInt(st.nextToken());
            switch (op) {
                case 1:
                    fullSquare.flipVertically();
                    break;
                case 2:
                    fullSquare.flipHorizontally();
                    break;
                case 3:
                    fullSquare.rotateRight(1);
                    break;
                case 4:
                    fullSquare.rotateRight(3);
                    break;
                case 5:
                    fullSquare.shiftRightOrder();
                    break;
                case 6:
                    fullSquare.shiftLeftOrder();
                    break;
            }
        }
        fullSquare.printResult();
    }

    static class FullSquare {
        public SubSquare[] subSquares;
        /*
         * 0 1
         * 3 2
         */
        public int[] order = new int[]{0, 1, 2, 3};

        FullSquare(int[][] board) {
            subSquares = new SubSquare[4];
            int[][][] boards = new int[4][N / 2][M / 2];
            for (int i = 0; i < N / 2; i++) {
                for (int j = 0; j < M / 2; j++) {
                    boards[0][i][j] = board[i][j];
                    boards[1][i][j] = board[i][M / 2 + j];
                    boards[2][i][j] = board[N / 2 + i][M / 2 + j];
                    boards[3][i][j] = board[N / 2 + i][j];
                }
            }
            for (int i = 0; i < 4; i++) {
                subSquares[i] = new SubSquare(boards[i]);
            }
        }

        public void flipHorizontally() {
            for (SubSquare subSquare : subSquares) {
                subSquare.flipHorizontally();
            }
            swapOrder(0, 1);
            swapOrder(2, 3);
        }

        public void flipVertically() {
            for (SubSquare subSquare : subSquares) {
                subSquare.flipVertically();
            }
            swapOrder(0, 3);
            swapOrder(1, 2);
        }

        public void rotateRightAngle() {
            for (SubSquare subSquare : subSquares) {
                subSquare.rotate(1);
            }
            shiftRightOrder();
        }

        public void rotateRight(int time) {
            for (int i = 0; i < time; i++) {
                rotateRightAngle();
            }
        }

        public void printSquares() {
            for (int idx : order) {
                System.out.println(subSquares[idx]);
            }
        }

        private void swapOrder(int a, int b) {
            order[a] += order[b];
            order[b] = order[a] - order[b];
            order[a] = order[a] - order[b];
        }

        private void shiftRightOrder() {
            for (int i = 1; i < order.length; i++) {
                swapOrder(0, i);
            }
        }

        public void shiftLeftOrder() {
            for (int i = 1; i < order.length; i++) {
                swapOrder(order.length - 1 - i, order.length - 1);
            }
        }

        public void printResult() {
            List<String> sub1Strings = subSquares[order[0]].toStrings();
            List<String> sub2Strings = subSquares[order[1]].toStrings();
            List<String> sub3Strings = subSquares[order[2]].toStrings();
            List<String> sub4Strings = subSquares[order[3]].toStrings();
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < sub1Strings.size(); i++) {
                result.append(sub1Strings.get(i)).append(sub2Strings.get(i)).append("\n");
            }
            for (int i = 0; i < sub3Strings.size(); i++) {
                result.append(sub4Strings.get(i)).append(sub3Strings.get(i)).append("\n");
            }
            System.out.println(result);
        }
    }

    static class SubSquare {
        public final int[][] board;
        public boolean isFlippedHorizontally;
        public boolean isFlippedVertically;
        public int rotationCount;

        SubSquare(int[][] board) {
            this.board = board;
        }

        public void flipHorizontally() {
            if (rotationCount % 2 == 0) {
                this.isFlippedHorizontally = !this.isFlippedHorizontally;
            } else {
                this.isFlippedVertically = !this.isFlippedVertically;
            }
        }

        public void flipVertically() {
            if (rotationCount % 2 == 0) {
                this.isFlippedVertically = !this.isFlippedVertically;
            } else {
                this.isFlippedHorizontally = !this.isFlippedHorizontally;
            }
        }

        public void rotate(int time) {
            this.rotationCount += time;
        }

        @Override
        public String toString() {
            StringBuilder result = new StringBuilder();
            int[][] resultBoard = getBoard();
            for (int[] row : resultBoard) {
                result.append(Arrays.toString(row)).append("\n");
            }
            return result.toString();
        }

        public int[][] getBoard() {
            int[][] result = copyBoard();
            if (isFlippedHorizontally) {
                result = flippedHorizontally(result);
            }
            if (isFlippedVertically) {
                result = flippedVertically(result);
            }
            for (int i = 0; i < rotationCount % 4; i++) {
                result = rotatedRightAngle(result);
            }
            return result;
        }

        private int[][] copyBoard() {
            int n = board.length;
            int m = board[0].length;
            int[][] result = new int[n][m];
            for (int i = 0; i < n; i++) {
                result[i] = Arrays.copyOf(board[i], m);
            }
            return result;
        }

        private int[][] flippedHorizontally(int[][] board) {
            int n = board.length;
            int m = board[0].length;
            int[][] result = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    result[i][m - 1 - j] = board[i][j];
                }
            }
            return result;
        }

        private int[][] flippedVertically(int[][] board) {
            int n = board.length;
            int m = board[0].length;
            int[][] result = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    result[n - 1 - i][j] = board[i][j];
                }
            }
            return result;
        }

        private int[][] rotatedRightAngle(int[][] board) {
            int n = board.length;
            int m = board[0].length;
            int[][] result = new int[m][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    result[j][n - 1 - i] = board[i][j];
                }
            }
            return result;
        }

        public List<String> toStrings() {
            int[][] resultBoard = getBoard();
            List<String> result = new ArrayList<>();
            for (int[] row : resultBoard) {
                StringBuilder sb = new StringBuilder();
                for (int e: row) {
                    sb.append(e).append(" ");
                }
                result.add(sb.toString());
            }
            return result;
        }
    }
}