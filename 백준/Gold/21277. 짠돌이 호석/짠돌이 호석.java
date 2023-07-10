import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static int N1, M1;
    public static int[][] puzzle1;
    public static int[][] puzzle1R1;
    public static int[][] puzzle1R2;
    public static int[][] puzzle1R3;
    public static int puzzle1Size;
    public static int N2, M2;
    public static int[][] puzzle2;
    public static int frameN, frameM;
    public static int[][] frame;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        initPuzzle1(br);
        initPuzzle2(br);
        puzzle1R1 = rotateBoard(puzzle1);
        puzzle1R2 = rotateBoard(puzzle1R1);
        puzzle1R3 = rotateBoard(puzzle1R2);
        createFrame();
//        printBoard(puzzle1);
//        System.out.println();
//        printBoard(puzzle2);
//        System.out.println();
//        printBoard(frame);
        System.out.println(solution());
    }

    private static void initPuzzle1(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N1 = Integer.parseInt(st.nextToken());
        M1 = Integer.parseInt(st.nextToken());
        puzzle1 = new int[N1][M1];
        for (int i = 0; i < N1; i++) {
            String inputLine = br.readLine();
            for (int j = 0; j < M1; j++) {
                puzzle1[i][j] = Integer.parseInt(String.valueOf(inputLine.charAt(j)));
            }
        }
    }

    private static void initPuzzle2(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N2 = Integer.parseInt(st.nextToken());
        M2 = Integer.parseInt(st.nextToken());
        puzzle2 = new int[N2][M2];
        for (int i = 0; i < N2; i++) {
            String inputLine = br.readLine();
            for (int j = 0; j < M2; j++) {
                puzzle2[i][j] = Integer.parseInt(String.valueOf(inputLine.charAt(j)));
            }
        }
    }

    private static void printBoard(int[][] board) {
        for (int[] row : board) {
            System.out.println(Arrays.toString(row));
        }
    }

    private static void createFrame() {
        puzzle1Size = Math.max(N1, M1);
        frameN = 2 * puzzle1Size + N2;
        frameM = 2 * puzzle1Size + M2;
        frame = new int[frameN][frameM];

        for (int i = 0; i < N2; i++) {
            for (int j = 0; j < M2; j++) {
                frame[i + puzzle1Size][j + puzzle1Size] = puzzle2[i][j];
            }
        }
    }
    private static int[][] rotateBoard(int[][] board){
        int r = board[0].length;
        int c = board.length;

        int[][] result = new int[r][c];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                result[j][c - 1 - i] = board[i][j];
            }
        }
        return result;
    }

    private static int solution() {
        int result = frameN * frameM;
        for (int i = 0; i < puzzle1Size + N2; i++) {
            for (int j = 0; j < puzzle1Size + M2; j++) {
                ArrayList<Integer> cadid = new ArrayList<>();
                cadid.add(result);
                cadid.add(tryInsert(puzzle1, i, j));
                cadid.add(tryInsert(puzzle1R1, i, j));
                cadid.add(tryInsert(puzzle1R2, i, j));
                cadid.add(tryInsert(puzzle1R3, i, j));
                result = cadid.stream().min(Integer::compare).orElseThrow();
            }
        }
        return result;
    }

    private static int tryInsert(int[][] puzzle, int r, int c) {
//        System.out.println();
//        System.out.println("r = " + r);
//        System.out.println("c = " + c);
        int result = 0;
//        printBoard(puzzle)
        int n = puzzle.length;
        int m = puzzle[0].length;
        int minR = puzzle1Size;
        int maxR = puzzle1Size + N2 - 1;
        int minC = puzzle1Size;
        int maxC = puzzle1Size + M2 - 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (puzzle[i][j] == 1) {
                    minR = Math.min(minR, r + i);
                    minC = Math.min(minC, c + j);
                    maxR = Math.max(maxR, r + i);
                    maxC = Math.max(maxC, c + j);
                }
                if (puzzle[i][j] == 1 && frame[r + i][c + j] == 1) {
                    return frameN * frameM;
                }
            }
        }
//        System.out.println(maxR);
//        System.out.println(minR);
//        System.out.println(maxC);
//        System.out.println(minC);
//        System.out.println((maxR - minR + 1) * (maxC - minC + 1));
        return (maxR - minR + 1) * (maxC - minC + 1);
    }
}
