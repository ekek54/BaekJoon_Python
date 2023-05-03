import java.util.*;
class Solution {
    public double[] solution(int k, int[][] ranges) {
        double[] answer = new double[ranges.length];
        ArrayList<Integer> collatzList = new ArrayList<>();
        collatzList.add(k);
        while (k != 1){
            if (k % 2 == 0){
                k /= 2;
            }
            else{
                k = k * 3 + 1;
            }
            collatzList.add(k);
        }
        double[] areas = new double[collatzList.size() - 1];
        for (int i = 0; i < collatzList.size() - 1; i++){
            areas[i] = ((double)collatzList.get(i) + collatzList.get(i + 1)) / 2;
        }
        
        for (int i = 0; i < ranges.length; i ++){
            int start = ranges[i][0];
            int end = areas.length + ranges[i][1];
            System.out.println("" + start + " " + end);
            if (end < start){
                answer[i] = -1;
            }
            else if (end == start){
                answer[i] = 0;
            }
            else{
                for (int j = start; j < end; j++){
                    answer[i] += areas[j];
                }
            }
        }
        System.out.println(Arrays.toString(areas));
        return answer;
    }
}