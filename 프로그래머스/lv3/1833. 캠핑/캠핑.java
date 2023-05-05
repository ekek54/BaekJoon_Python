import java.util.*;
class Solution {
    public int solution(int n, int[][] data) {
        int answer = 0;
        Arrays.sort(data, (o1, o2) -> {
            return o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1];
        });
        for(int i = 0; i < n; i ++){
            int l = 0;
            int r = 2147483647;
            int prer = r;
            int cur_row = data[i][0];
            for(int j = i + 1; j < n; j ++){
                if (data[i][0] == data[j][0]) continue;
                if (data[i][1] == data[j][1]) continue;
                if (data[i][1] > data[j][1] && l <= data[j][1]){
                    answer += 1;
                    l = data[j][1];
                }
                else if (data[i][1] < data[j][1]){
                    if (r >= data[j][1]){
                        answer += 1;
                        prer = r;
                        r = data[j][1];
                        cur_row = data[j][0];
                    }
                    else if(cur_row == data[j][0] && data[j][1] <= prer){
                        answer += 1;                        
                    }
                }
                
            }
        }
        return answer;
    }
}