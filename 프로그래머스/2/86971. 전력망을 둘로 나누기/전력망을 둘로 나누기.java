import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < n - 1; i++) {
            DisjointSet disjointSet = new DisjointSet(n);
            for (int j = 0; j < n - 1; j++) {
                if (j == i) continue;
                disjointSet.union(wires[j][0] - 1, wires[j][1] - 1);
            }
            answer = Math.min(answer, Math.abs(n - 2 * disjointSet.sizeOf(0)));
        }
        return answer;
    }
}

class DisjointSet {
    private int N;
    private int[] parent;
    
    public DisjointSet(int N) {
        this.N = N;
        this.parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }
    }
    
    private int find(int a) {
        if (a == parent[a]) return a;
        parent[a] = find(parent[a]);
        return parent[a];
    }
    
    public boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a > b) {
            parent[a] = b;
            return true;
        }
        if (a == b) {
            return false;
        }
        parent[b] = a;
        return true;
    }
    
    public int sizeOf(int idx) {
        int root = find(idx);
        int result = 0;
        for (int i = 0; i < N; i++) {
            if (root == find(i)) result++;
        }
        // System.out.println(Arrays.toString(parent));
        return result;
    }
}