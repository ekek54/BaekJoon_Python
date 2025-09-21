import java.io.*;
import java.math.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder moveSB = new StringBuilder();
    private static int answer = 0;
    
    public static void main(String[] args) throws IOException{
        int N = Integer.parseInt(br.readLine());
        if (N <= 20) {
            hanoi(1, 3, N);
            System.out.println(answer);
            System.out.println(moveSB);   
        } else {
            System.out.println(hanoiCnt(N));
        }
    }
    
    private static void hanoi(int src, int des, int size) {
        if (size == 1) {
            appendMove(src, des);
            return;
        }
        int remain = 6 - (src + des);
        hanoi(src, remain, size - 1);
        appendMove(src, des);
        hanoi(remain, des, size - 1);
        return;
    }
    
    private static void appendMove(int src, int des) {
        answer++;
        moveSB.append(src).append(" ").append(des);
        moveSB.append("\n");
        return;
    }
    
    private static BigInteger hanoiCnt(int size) {
        BigInteger res = new BigInteger("1");
        for (int i = 1; i < size; i++) {
            res = res.multiply(new BigInteger("2")).add(new BigInteger("1"));
        }
        return res;
    }
}
