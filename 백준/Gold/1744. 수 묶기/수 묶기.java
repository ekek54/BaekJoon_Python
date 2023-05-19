import java.util.*;

public class Main {
    static int N;
    static ArrayList<Integer> positives = new ArrayList<>();
    static ArrayList<Integer> negatives = new ArrayList<>();

    public static void main(String[] args) {
        init();
        System.out.println(positiveSum() + negativeSum());
        //System.out.println(positives.toString());
        //System.out.println(negatives.toString());
    }

    static void init() {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            if (num <= 0) negatives.add(num);
            else positives.add(num);
        }
    }

    static int positiveSum() {
        int result = 0;
        positives.sort(Comparator.reverseOrder());
        for (int i = 0; i < positives.size(); i += 2) {
            if (i + 1 < positives.size()
                    && positives.get(i) != 1
                    && positives.get(i + 1) != 1) {
                result += positives.get(i) * positives.get(i + 1);
            } else if(i + 1 >= positives.size()) {
                result += positives.get(i);
            }else{
                result += positives.get(i);
                result += positives.get(i + 1);;
            }
        }
        return result;
    }

    static int negativeSum() {
        int result = 0;
        negatives.sort(Comparator.naturalOrder());
        for (int i =0; i < negatives.size(); i += 2) {
            if (i + 1 < negatives.size()) {
                result += negatives.get(i) * negatives.get(i + 1);
            }
            else {
                result += negatives.get(i);
            }
        }
        return result;
    }
}
