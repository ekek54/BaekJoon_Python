import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, C, M;
    static int[][] infoBoard;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(simulation());
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        infoBoard = new int[N][N];
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int amount = Integer.parseInt(st.nextToken());
            infoBoard[from - 1][to - 1] = amount;
        }
    }

    static int simulation() {
        int result = 0;
        int[] inventory = new int[N];
        int curHave = 0;
        for (int i = 0; i < N; i++) {
            //System.out.println(Arrays.toString(inventory));
            result += inventory[i];
            curHave -= inventory[i];
            inventory[i] = 0;
            curHave = load(inventory, curHave, i);
        }
        return result;
    }

    private static int load(int[] inventory, int curHave, int i) {
        int l = 0;
        int r = N - 1;
        while (l < N && curHave < C) {
            if (infoBoard[i][l] == 0) {
                l++;
                continue;
            }
            if (C - curHave >= infoBoard[i][l]) {
                inventory[l] += infoBoard[i][l];
                curHave += infoBoard[i][l];
                infoBoard[i][l] = 0;
            } else {
                inventory[l] += C - curHave;
                infoBoard[i][l] -= C - curHave;
                curHave = C;
            }
        }
        while (l < r) {
            if (infoBoard[i][l] == 0) {
                l++;
                continue;
            }
            if (inventory[r] == 0) {
                r--;
                continue;
            }
            if (infoBoard[i][l] >= inventory[r]) {
                inventory[l] += inventory[r];
                infoBoard[i][l] -= inventory[r];
                inventory[r] = 0;
            } else {
                inventory[l] += infoBoard[i][l];
                inventory[r] -= infoBoard[i][l];
                infoBoard[i][l] = 0;
            }
        }
        return curHave;
    }
}
