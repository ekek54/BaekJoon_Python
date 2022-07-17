# [Gold IV] 감시 - 15683 

[문제 링크](https://www.acmicpc.net/problem/15683) 

### 성능 요약

메모리: 177124 KB, 시간: 2536 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다. 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.</p>

<table class="table table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 20%; text-align: center; vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/1.png" style="width: 113px; height: 70px;"></td>
			<td style="width: 20%; text-align: center;vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/2.png" style="width: 156px; height: 70px;"></td>
			<td style="width: 20%; text-align: center;vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/3.png" style="width: 100px; height: 100px;"></td>
			<td style="width: 20%; text-align: center;vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/4.png" style="width: 138px; height: 100px;"></td>
			<td style="width: 20%; text-align: center;vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/5.png" style="width: 149px; height: 150px;"></td>
		</tr>
		<tr>
			<td style="width: 20%; text-align: center;">1번</td>
			<td style="width: 20%; text-align: center;">2번</td>
			<td style="width: 20%; text-align: center;">3번</td>
			<td style="width: 20%; text-align: center;">4번</td>
			<td style="width: 20%; text-align: center;">5번</td>
		</tr>
	</tbody>
</table>

<p>1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.</p>

<p>CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. CCTV가 감시할 수 없는 영역은 사각지대라고 한다.</p>

<p>CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.</p>

<pre>0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0</pre>

<p>지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 위의 예시에서 1번의 방향에 따라 감시할 수 있는 영역을 '<code>#</code>'로 나타내면 아래와 같다.</p>

<table class="table table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 25%; text-align: center;">
			<pre>0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 # 6 0
0 0 0 0 0 0</pre>
			</td>
			<td style="width: 25%; text-align: center;">
			<pre>0 0 0 0 0 0
0 0 0 0 0 0
# # 1 0 6 0
0 0 0 0 0 0</pre>
			</td>
			<td style="width: 25%; text-align: center;">
			<pre>0 0 # 0 0 0
0 0 # 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0</pre>
			</td>
			<td style="width: 25%; text-align: center;">
			<pre>0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 # 0 0 0</pre>
			</td>
		</tr>
		<tr>
			<td style="width: 25%; text-align: center;">→</td>
			<td style="width: 25%; text-align: center;">←</td>
			<td style="width: 25%; text-align: center;">↑</td>
			<td style="width: 25%; text-align: center;">↓</td>
		</tr>
	</tbody>
</table>

<p>CCTV는 벽을 통과할 수 없기 때문에, 1번이 → 방향을 감시하고 있을 때는 6의 오른쪽에 있는 칸을 감시할 수 없다.</p>

<pre>0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5</pre>

<p>위의 예시에서 감시할 수 있는 방향을 알아보면 아래와 같다.</p>

<table class="table table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 25%; text-align: center;">
			<pre>0 0 0 0 0 #
# 2 # # # #
0 0 0 0 6 #
0 6 # # 2 #
0 0 0 0 0 #
# # # # # 5</pre>
			</td>
			<td style="width: 25%; text-align: center;">
			<pre>0 0 0 0 0 #
# 2 # # # #
0 0 0 0 6 #
0 6 0 0 2 #
0 0 0 0 # #
# # # # # 5</pre>
			</td>
			<td style="width: 25%; text-align: center;">
			<pre>0 # 0 0 0 #
0 2 0 0 0 #
0 # 0 0 6 #
0 6 # # 2 #
0 0 0 0 0 #
# # # # # 5</pre>
			</td>
			<td style="width: 25%; text-align: center;">
			<pre>0 # 0 0 0 #
0 2 0 0 0 #
0 # 0 0 6 #
0 6 0 0 2 #
0 0 0 0 # #
# # # # # 5</pre>
			</td>
		</tr>
		<tr>
			<td style="width: 25%; text-align: center;">왼쪽 상단 2: ↔, 오른쪽 하단 2: ↔</td>
			<td style="width: 25%; text-align: center;">왼쪽 상단 2: ↔, 오른쪽 하단 2: ↕</td>
			<td style="width: 25%; text-align: center;">왼쪽 상단 2: ↕, 오른쪽 하단 2: ↔</td>
			<td style="width: 25%; text-align: center;">왼쪽 상단 2: ↕, 오른쪽 하단 2: ↕</td>
		</tr>
	</tbody>
</table>

<p>CCTV는 CCTV를 통과할 수 있다. 아래 예시를 보자.</p>

<pre>0 0 2 0 3
0 6 0 0 0
0 0 6 6 0
0 0 0 0 0
</pre>

<p>위와 같은 경우에 2의 방향이 ↕ 3의 방향이 ←와 ↓인 경우 감시받는 영역은 다음과 같다.</p>

<pre># # 2 # 3
0 6 # 0 #
0 0 6 6 #
0 0 0 0 #
</pre>

<p>사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)</p>

<p>둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. </p>

<p>CCTV의 최대 개수는 8개를 넘지 않는다.</p>

### 출력 

 <p>첫째 줄에 사각 지대의 최소 크기를 출력한다.</p>

### 풀이 과정

dfs를 이용한 완전탐색 문제이다. 카메라의 모델을 depth 각각의 방향을 width로하는 상태트리를 완전탐색하여 모든 경우의 수를 구할 수 있다.
dfs와 방향벡터를 잘 이용할 수 있다면 쉽게 풀 수 있다.

### 구현 과정 

2차원 배열에서의 dfs는 다음 depth의 dfs를 실행한 후 종료 될 떄 원상태의 2차원 배열로 돌아와야 한다.
이를위해 deepcopy를 통해 원본 배열을 저장해놓는데 이러면 배열크기가 큰 경우에 시간 초과가 발생하는 경우가 더러 있었다.
배열이 mutable 객체라 call by referance이기 때문에 발생하는 문제인데 이를 효율적으로 처리하는 방법이 있나 찾아보았지만 없는 것 같다.