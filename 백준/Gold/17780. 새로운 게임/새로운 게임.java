import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static final int MAX_ANSWER = 1000;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, K;
    static Square[][] board;
    static List<Piece> pieceList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        int answer = 0;
        do {
            answer++;
            pieceList.forEach(Piece::move);
        } while (!isGameOver() && answer <= MAX_ANSWER);
        System.out.println(answer <= MAX_ANSWER ? answer : -1);
    }

    private static boolean isGameOver() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j].pieceStack.size() >= 4) return true;
            }
        }
        return false;
    }

    private static void init() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        initBoard(br);
        initPieces();
    }

    private static void initPieces() throws IOException {
        StringTokenizer st;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int di = Integer.parseInt(st.nextToken()) - 1;
            Piece piece = new Piece(r, c, i, Direction.fromIdx(di));
            pieceList.add(piece);
            board[r][c].pieceStack.add(piece);
        }
    }

    private static void initBoard(BufferedReader br) throws IOException {
        StringTokenizer st;
        board = new Square[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int colorIdx = Integer.parseInt(st.nextToken());
                board[i][j] = new Square(SquareColor.fromIdx(colorIdx));
            }
        }
    }

    static class Square {
        private final SquareColor color;
        private final List<Piece> pieceStack = new ArrayList<>();

        public Square(SquareColor color) {
            this.color = color;
        }

        @Override
        public String toString() {
            return "Square{" +
                    "pieceStack=" + pieceStack +
                    '}';
        }
    }

    static class Piece {
        public int r;
        public int c;
        public int number;
        public Direction direction;

        public Piece(int r, int c, int number, Direction direction) {
            this.r = r;
            this.c = c;
            this.number = number;
            this.direction = direction;
        }

        public void move() {
            if (!isBottom()) return;

            int nr = r + direction.getDr();
            int nc = c + direction.getDc();

            if (outOfBoard(nr, nc) || board[nr][nc].color == SquareColor.BLUE) {
                reversePiece();
                nr = r + direction.getDr();
                nc = c + direction.getDc();
                if (outOfBoard(nr, nc) || board[nr][nc].color == SquareColor.BLUE) return;
            }
            if (board[nr][nc].color == SquareColor.WHITE) {
                movePiecesToNext(nr, nc);
                return;
            }

            if (board[nr][nc].color == SquareColor.RED) {
                Collections.reverse(board[r][c].pieceStack);
                movePiecesToNext(nr, nc);
                return;
            }
        }

        private void movePiecesToNext(int nr, int nc) {
            List<Piece> curPieceStack = board[r][c].pieceStack;
            List<Piece> nxtPieceStack = board[nr][nc].pieceStack;
            nxtPieceStack.addAll(curPieceStack);
            curPieceStack.forEach((p) -> p.movePieceToNext(nr, nc));
            curPieceStack.clear();
        }

        private void movePieceToNext(int nr, int nc) {
            r = nr;
            c = nc;
        }

        private boolean isBottom() {
            return equals(board[r][c].pieceStack.get(0));
        }

        private void reversePiece() {
            if (direction == Direction.UP) {
                direction = Direction.DOWN;
                return;
            }
            if (direction == Direction.DOWN) {
                direction = Direction.UP;
                return;
            }
            if (direction == Direction.RIGHT) {
                direction = Direction.LEFT;
                return;
            }
            if (direction == Direction.LEFT) {
                direction = Direction.RIGHT;
                return;
            }
        }

        private static boolean outOfBoard(int nr, int nc) {
            return nr < 0 || N <= nr || nc < 0 || N <= nc;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj instanceof Piece) {
                Piece p = (Piece) obj;
                return p.number == number;
            }
            return false;
        }

        @Override
        public String toString() {
            return "Piece{" +
                    "number=" + number +
                    '}';
        }
    }

    private static void pb() {
        for (int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
        System.out.println(" @@@@@@@@@@@@@@@@@@@");
    }
}


enum SquareColor {
    WHITE, RED, BLUE;

    public static SquareColor fromIdx(int colorIdx) {
        for (SquareColor squareColor : SquareColor.values()) {
            if (squareColor.ordinal() == colorIdx) {
                return squareColor;
            }
        }
        throw new IllegalStateException("Invalid colorIdx");
    }
}

enum Direction {
    RIGHT(0, 1), LEFT(0, -1), UP(-1, 0), DOWN(1, 0);

    private final int dr;
    private final int dc;

    public int getDr() {
        return dr;
    }

    public int getDc() {
        return dc;
    }

    private Direction(int dr, int dc) {
        this.dr = dr;
        this.dc = dc;
    }

    public static Direction fromIdx(int di) {
        for (Direction directiion : Direction.values()) {
            if (directiion.ordinal() == di) {
                return directiion;
            }
        }
        throw new IllegalStateException("Invalid di");
    }
}