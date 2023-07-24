import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] targetPorts = new int[n];
        for (int i = 0; i < n; i++) {
            targetPorts[i] = sc.nextInt();
        }
//        System.out.println("arr = " + Arrays.toString(targetPorts));

        List<Integer> dp = new ArrayList<>();
        for (int targetPort : targetPorts) {
            insert(targetPort, dp);
        }
        System.out.println(dp.size());
    }
    public static void insert(int value, List<Integer> list) {
        int insertIdx = bisecRight(value, list);
        mySet(insertIdx, value, list);
    }

    //target 바로 다음 큰 수의 인덱스를 찾는 이진탐색
    public static int bisecRight(int target, List<Integer> list) {
        int l = 0;
        int r = list.size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (list.get(mid) > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }

    public static void mySet(int index, int value, List<Integer> list) {
        if (index < list.size()) list.set(index, value);
        else list.add(value);
    }
}
