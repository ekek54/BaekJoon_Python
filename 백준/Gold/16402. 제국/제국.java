import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static Map<String, Integer> kingdomIdx = new HashMap<>();
    static String[] kingdomNames;
    static int[] parent;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        init();
        StringTokenizer st;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), ",");
            String kingdom1 = st.nextToken();
            String kingdom2 = st.nextToken();
            int winIdx = Integer.parseInt(st.nextToken());
            String winner = winIdx == 1 ? kingdom1 : kingdom2;
            String loser = winIdx == 2 ? kingdom1 : kingdom2;
            union(winner, loser);
        }
        int independentCnt = 0;
        List<String> independents = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            if (parent[i] == i) {
                independentCnt++;
                independents.add(kingdomNames[i]);
            }
        }
        Collections.sort(independents);
        System.out.println(independentCnt);
        for (String independent : independents) {
            System.out.println(independent);
        }
    }

    private static void init() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        kingdomNames = new String[N];
        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }
        for (int i = 0; i < N; i++) {
            String kingdomName = br.readLine();
            kingdomIdx.put(kingdomName, i);
            kingdomNames[i] = kingdomName;
        }
    }

    private static int find(int a) {
        if (a == parent[a]) return a;
        parent[a] = find(parent[a]);
        return parent[a];
    }

    private static void union(String winner, String loser) {
        int rootWinnerIdx = find(kingdomIdx.get(winner));
        int rootLoserIdx = find(kingdomIdx.get(loser));
        if (rootWinnerIdx == rootLoserIdx) {
            int loserIdx = kingdomIdx.get(winner) == rootWinnerIdx ? kingdomIdx.get(loser) : kingdomIdx.get(winner);
            kingdomNames[rootWinnerIdx] = winner;
            kingdomIdx.put(winner, rootWinnerIdx);
            kingdomNames[loserIdx] = loser;
            kingdomIdx.put(loser, loserIdx);
        } else {
            parent[rootLoserIdx] = rootWinnerIdx;
        }
    }
}
