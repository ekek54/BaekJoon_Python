import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int G = sc.nextInt();
        int idx = 1;
        boolean flag = false;
        while (G >= Math.pow(idx + 1, 2) - Math.pow(idx, 2)) {
            double C = Math.sqrt(G + Math.pow(idx, 2));
            if (isInteger(C)) {
                flag = true;
                System.out.println((int) C);
            }
            idx++;
        }
        if(!flag) System.out.println(-1);
    }

    public static boolean isInteger(double num) {
        return num % 1 == 0.0;
    }
}
