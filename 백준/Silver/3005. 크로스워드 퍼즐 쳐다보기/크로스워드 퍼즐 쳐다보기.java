import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int R, C;
    static char[][] puzzle;

    public static void main(String[] args) throws IOException {
        init();
        ArrayList<String> wordList = parsePuzzle();
        wordList.sort(String::compareTo);
//        System.out.println("wordList = " + wordList);
        System.out.println(wordList.get(0));

    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        puzzle = new char[R][C];

        for (int i = 0; i < R; i++) {
            String inputLine = br.readLine();
            for (int j = 0; j < C; j++) {
                puzzle[i][j] = inputLine.charAt(j);
            }
        }
    }

    public static ArrayList<String> parsePuzzle() {
        ArrayList<String> result = new ArrayList<>();
        StringBuilder sb;
        parseRow(result);
        parseCol(result);
        return result;
    }

    private static void parseRow(ArrayList<String> result) {
        StringBuilder sb;
        for (int i = 0; i < R; i++) {
            sb = new StringBuilder();
            for (int j = 0; j < C; j++) {
                if (puzzle[i][j] == '#') {
                    if (sb.length() >= 2) {
                        result.add(sb.toString());
                    } else if (sb.length() > 0) {
                        sb = new StringBuilder();
                    }
                } else {
                    sb.append(puzzle[i][j]);
                }
            }
            if (sb.length() >= 2) {
                result.add(sb.toString());
            }
        }
    }

    private static void parseCol(ArrayList<String> result) {
        StringBuilder sb;
        for (int i = 0; i < C; i++) {
            sb = new StringBuilder();
            for (int j = 0; j < R; j++) {
                if (puzzle[j][i] == '#') {
                    if (sb.length() >= 2) {
                        result.add(sb.toString());
                    } else if (sb.length() > 0) {
                        sb = new StringBuilder();
                    }
                } else {
                    sb.append(puzzle[j][i]);
                }
            }
            if (sb.length() >= 2) {
                result.add(sb.toString());
            }
        }
    }
}
