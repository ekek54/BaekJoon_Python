import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static char[][] board;
    static int redR, redC, blueR, blueC;
    static int holeR, holeC;

    static HashMap<State,Boolean> visit = new HashMap<>();

    public static void main(String[] args) throws IOException {
        init();
        //pb();
        String answer = bfs().moves;
        if (answer != null) {
            System.out.println(answer.length());
        }else{
            System.out.println(-1);
        }
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];
        for (int i = 0; i < N; i++) {
            String inputLine = br.readLine();
            for (int j = 0; j < M; j++) {
                if (inputLine.charAt(j) == 'R') {
                    redR = i;
                    redC = j;
                    board[i][j] = '.';
                } else if (inputLine.charAt(j) == 'B') {
                    blueR = i;
                    blueC = j;
                    board[i][j] = '.';
                } else if (inputLine.charAt(j) == 'O') {
                    holeR = i;
                    holeC = j;
                    board[i][j] = inputLine.charAt(j);
                } else {
                    board[i][j] = inputLine.charAt(j);
                }
            }
        }
    }

    static State bfs() {
        Queue<State> que = new LinkedList<>();
        State startState = new State(redR, redC, blueR, blueC, "");
        que.add(startState);
        while (!que.isEmpty()) {
            State curState = que.poll();
            //System.out.println(curState);
            if (curState.redInHole()) return curState;
            //if (curState.moves.length() == 10) continue;
            for (int i = 0; i < 4; i++) {
                State nxtState = curState.move(i);
                if (nxtState.blueInHole()) continue;
                if (visit.containsKey(nxtState)) continue;
                visit.put(nxtState, true);
                que.add(nxtState);
            }
        }
        return new State();
    }

    static void pb() {
        for (int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }
}

class State {
    int redR, redC, blueR, blueC;
    String moves;

    public State() {
    }

    public State(int redR, int redC, int blueR, int blueC, String moves) {
        this.redR = redR;
        this.redC = redC;
        this.blueR = blueR;
        this.blueC = blueC;
        this.moves = moves;
    }

    public State(State state) {
        this.redR = state.redR;
        this.redC = state.redC;
        this.blueR = state.blueR;
        this.blueC = state.blueC;
        this.moves = new String(state.moves);
    }

    public State move(int di) {
        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};
        String[] direction = {"R", "L", "D", "U"};
        State result = new State(this);
        result.moves += direction[di];
        moveRed(di, dr, dc, result);
        moveBlue(di, dr, dc, result);
        moveRed(di, dr, dc, result);
        return result;
    }

    private static void moveBlue(int di, int[] dr, int[] dc, State result) {
        while (true) {
            if (result.blueInHole()) break;
            int nxtBlueR = result.blueR + dr[di];
            int nxtBlueC = result.blueC + dc[di];
            if (Main.board[nxtBlueR][nxtBlueC] == '#') break;
            if (nxtBlueR == result.redR && nxtBlueC == result.redC && !result.redInHole()) break;
            result.blueR = nxtBlueR;
            result.blueC = nxtBlueC;
        }
    }

    private static void moveRed(int di, int[] dr, int[] dc, State result) {
        while (true) {
            if (result.redInHole()) break;
            int nxtRedR = result.redR + dr[di];
            int nxtRedC = result.redC + dc[di];
            if (Main.board[nxtRedR][nxtRedC] == '#') break;
            if (nxtRedR == result.blueR && nxtRedC == result.blueC && !result.blueInHole()) break;
            result.redR = nxtRedR;
            result.redC = nxtRedC;
        }
    }

    public boolean blueInHole() {
        return blueR == Main.holeR && blueC == Main.holeC;
    }

    public boolean redInHole() {
        return redR == Main.holeR && redC == Main.holeC;
    }

    @Override
    public String toString() {
        return "boj.State{" +
                "redR=" + redR +
                ", redC=" + redC +
                ", blueR=" + blueR +
                ", blueC=" + blueC +
                ", moves='" + moves + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        State state = (State) o;
        return redR == state.redR && redC == state.redC && blueR == state.blueR && blueC == state.blueC;
    }

    @Override
    public int hashCode() {
        return Objects.hash(redR, redC, blueR, blueC);
    }
}