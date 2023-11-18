import java.util.*;

class Solution {
    static int n;
    
    public int solution(int n, int[][] lighthouse) {
        Solution.n = n;
        List<List<Integer>> adjList = initAdjList(lighthouse);
        int[] indegree = new int[n];
        Queue<Integer> leafQue = getLeafQue(adjList, indegree);
        int[][] dp = bottomUp(adjList, leafQue, indegree);
        return Math.min(dp[0][0], dp[0][1]);
    }
    
    private int[][] bottomUp(List<List<Integer>> adjList, Queue<Integer> leafQue, int[] indegree) {
        int[][] dp = new int[n][2];
        for (int i = 0; i < n; i++) {
            dp[i][1] = 1;
        }
        
        while (!leafQue.isEmpty()) {
            int cur = leafQue.poll();
            for (Integer nxt : adjList.get(cur)) {
                if (indegree[nxt] != 0) {
                    if (--indegree[nxt] == 0) {
                        leafQue.add(nxt);
                    }
                    dp[nxt][0] += dp[cur][1];
                    dp[nxt][1] += Math.min(dp[cur][0], dp[cur][1]);
                }
            }
        }
        return dp;
    }
    
    private void printBoard(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }
    
    private Queue<Integer> getLeafQue(List<List<Integer>> adjList, int[] indegree) {
        Queue<Integer> que = new LinkedList<>();
        Queue<Integer> leaf = new LinkedList<>();
        boolean[] visit = new boolean[n];
        visit[0] = true;
        que.add(0);
        while (!que.isEmpty()) {
            int cur = que.poll();
            boolean isLeaf = true;
            for (Integer nxt : adjList.get(cur)) {
                if (!visit[nxt]) {
                    indegree[cur]++;
                    visit[nxt] = true;
                    que.add(nxt);
                    isLeaf = false;
                }
            }
            if (isLeaf) {
                leaf.add(cur);
            }
        }
        return leaf;
    }
    
    private List<List<Integer>> initAdjList(int[][] lighthouse) {
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<Integer>());
        }
        for (int[] edge : lighthouse) {
            int a = edge[0] - 1;
            int b = edge[1] - 1;
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }
        return adjList;
    }
}