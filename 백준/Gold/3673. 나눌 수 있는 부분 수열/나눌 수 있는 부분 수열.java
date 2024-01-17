import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int[] modCnt = new int[1000001];	//modCnt[i] : 누적합을 d로 나눴을 때 나머지 i가 나온 횟수
		                       
		for(int t = 1; t<=T; t++) {
			String[] dn = br.readLine().split(" ");
			int d = Integer.parseInt(dn[0]);	//나누는 수
			int n = Integer.parseInt(dn[1]);	//수열의 크기
			
			Arrays.fill(modCnt, 0);		//배열 초기화
			
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int num = 0;
			long sum = 0;	//누적합
			for(int i = 0; i<n; i++) {
				num = Integer.parseInt(st.nextToken());
				sum += num;
				int k = (int)(sum % d);
				modCnt[k]++;
			}
			
			long count = modCnt[0];
			for(int i = 0; i<=d; i++) {
				long cur = modCnt[i];
				count += cur * (cur - 1) / 2;
			}
			
			sb.append(count).append("\n");
		}
		System.out.println(sb);
	}
}