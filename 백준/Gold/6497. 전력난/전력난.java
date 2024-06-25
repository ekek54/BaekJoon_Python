import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        while (true) {
            StringTokenizer st= new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            if (m == 0) return;
            DisjointSet disjointSet = new DisjointSet(m);
            PriorityQueue<Road> pq = new PriorityQueue<>((r1, r2) -> {
                return r1.length - r2.length;
            });
            int totalLength = 0;
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int z = Integer.parseInt(st.nextToken());
                Road road = new Road(x, y, z);
                totalLength += road.length;
                pq.add(road);
            }

            int used = 0;
            while(!pq.isEmpty()) {
                Road road = pq.poll();
                if (disjointSet.union(road.v1, road.v2)) {
                    used += road.length;
                }
            }
            System.out.println(totalLength - used);
        }
    }


    static class Road {
        public int v1, v2;
        public int length;

        public Road(int v1, int v2, int length) {
            this.v1 = v1;
            this.v2 = v2;
            this.length = length;
        }

        @Override
        public String toString() {
            return "Road{" +
                    "v1=" + v1 +
                    ", v2=" + v2 +
                    ", length=" + length +
                    '}';
        }
    }

    static class DisjointSet {
        public int[] parent;

        public DisjointSet(int size) {
            parent = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
        }

        public int find(int a) {
            if (parent[a] == a) return a;
            parent[a] = find(parent[a]);
            return parent[a];
        }

        public boolean union(int a, int b) {
            a = find(a);
            b = find(b);
            if (a < b) {
                parent[b] = a;
                return true;
            }
            if (a > b) {
                parent[a] = b;
                return true;
            }
            return false;
        }
    }
}
