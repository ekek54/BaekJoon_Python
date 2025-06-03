import java.io.*;
import java.util.*;

class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        for(int i = 1; i < N; i++) {
			
			// 각 라운드별 비교횟수는 배열 크기의 현재 라운드를 뺀 만큼 비교함
			for(int j = 0; j < N - i; j++) {
				
				/*
				 *  현재 원소가 다음 원소보다 클 경우
				 *  서로 원소의 위치를 교환한다. 
				 */
				if(arr[j] > arr[j + 1]) {
                    int tmp = arr[j];
					arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
				}
			}
		}
        for (int i = 0; i < N; i++) {
            System.out.println(arr[i]);
        }
    }
}