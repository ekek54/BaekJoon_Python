import java.util.*;

class Solution {
    private List<Edge> edges;
    private int[] nodes;
    private Map<Integer, Integer> parent = new HashMap<>();
    private Map<Integer, List<Integer>> adjs = new HashMap<>();
    private Map<Integer, Map<Integer, Integer>> forest = new HashMap<>();
    
    public int[] solution(int[] nodes, int[][] edges) {
        int[] answer = {};
        this.nodes = nodes;
        this.edges = preprocess(edges);
        for (int node : nodes) {
            parent.put(node, node);
        }
        unionEdges();
        initAdjs();
        initForest();
        return cntTrees();
    }
    
    private int[] cntTrees() {
        int cnt = 0;
        int reverseCnt = 0;
            
        for (Integer key : forest.keySet()) {
            Map<Integer, Integer> tree = forest.get(key);
            int match = 0;
            int nonMatch = 0;
            for (Integer node : tree.keySet()) {
                if (node % 2  == tree.get(node) % 2) {
                    match++;
                } else {
                    nonMatch++;
                }
            }
            if (match == 1) {
                cnt++;
            }
            if (nonMatch == 1) {
                reverseCnt++;
            }
        }
        return new int[] {cnt, reverseCnt};
    }
    
    private void initForest() {
        for (int node : parent.keySet()) {
            int parent = find(node);
            // System.out.println("" + node + ", " + parent);
            // System.out.println(adjs.get(node));
            if (!forest.containsKey(parent)) {
                Map<Integer, Integer> tree = new HashMap<>();
                tree.put(node, adjs.get(node).size());
                forest.put(parent, tree);
            } else {
                Map<Integer, Integer> tree = forest.get(parent);
                tree.put(node, adjs.get(node).size());
            }
        }
        return;
    }
    
    private void initAdjs() {
        for (int node : nodes) {
            List<Integer> adjList = new ArrayList<>();
            adjs.put(node, adjList);
        }
        for (Edge edge : edges) {
            adjs.get(edge.a).add(edge.b);
            adjs.get(edge.b).add(edge.a);
        }
    }
    
    private void addAdj(int a, int b) {
        if (!adjs.containsKey(a)) {
                List<Integer> adjList = new ArrayList<>();
                adjList.add(b);
                adjs.put(a, adjList);
            } else {
                adjs.get(a).add(b);
            }
    }
    
    private void unionEdges() {
        for (Edge edge : edges) {
            union(edge.a, edge.b);
        }
        for (int node : nodes) {
            find(node);
        }
    }
    
    private int find(int a) {
        if (a == parent.get(a)) return a;
        parent.put(a, find(parent.get(a)));
        return parent.get(a);
    }
    
    private boolean union (int a, int b) {
        a = find(a);
        b = find(b);
        
        if (a < b) {
            parent.put(b, a);
            return true;
        }
        if (b < a) {
            parent.put(a, b);
            return true;
        }
        return false;
    }
    
    //중복 제거
    private List<Edge> preprocess(int[][] edges) {
        Set<Edge> result = new HashSet<>();
        for (int[] edge : edges) {
            Edge e = new Edge(edge);
            result.add(e);
        }
        
        return new ArrayList<>(result);
    }
    
    
}

class Edge {
    public int a, b;
    
    public Edge (int[] edge) {
        Arrays.sort(edge);
        this.a = edge[0];
        this.b = edge[1];
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Edge)) {
          return false;  
        }
        Edge e = (Edge) o;
        return this.a == e.a && this.b == e.b;
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(a, b);
    }
    
    @Override
    public String toString() {
        return "{" + a + ", " + b + "}";
    }
}
