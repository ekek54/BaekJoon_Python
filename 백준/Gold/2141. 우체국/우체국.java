import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] towns;

    public static void main(String[] args) {
        init();
        //pb(towns);
        System.out.println(leftBiSec());
    }

    static void init() {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        sc.nextLine();
        towns = new int[N][2];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(sc.nextLine());
            towns[i][0] = Integer.parseInt(st.nextToken());
            towns[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(towns, (e1, e2) -> {
            return e1[0] - e2[0];
        });
    }

    static void pb(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }

    static long calc(int mid) {
        long result = 0;
        for (int[] town : towns) {
            result += (long) town[1] * Math.abs(town[0] - mid);
        }
        return result;
    }

    static int leftBiSec() {
        int l = (int) -1000000000;
        int r = (int) 1000000000;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (calc(mid) >= calc(mid - 1)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }

}

