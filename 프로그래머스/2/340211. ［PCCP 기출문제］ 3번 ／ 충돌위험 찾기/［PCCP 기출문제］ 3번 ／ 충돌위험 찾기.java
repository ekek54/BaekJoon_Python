import java.util.*;

class Solution {
    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        List<List<Point>> paths = new ArrayList<>();
        for (int[] route: routes) {
            paths.add(getPath(points, route));
        }
        // System.out.println(paths);
        return cntDangerous(paths);
    }
    
    public int cntDangerous(List<List<Point>> paths) {
        int maxSize = paths.stream().map(path -> path.size()).max(Integer::compare).get();
        int res = 0;
        for (int i = 0; i < maxSize; i++) {
            Map<Point, Integer> counter = new HashMap<>();
            for (List<Point> path: paths) {
                if (path.size() > i) {
                    if (counter.containsKey(path.get(i))) {
                        counter.put(path.get(i), counter.get(path.get(i)) + 1);
                    } else {
                        counter.put(path.get(i), 1);
                    }
                }
            }
            // System.out.println(counter);
            for (Point p: counter.keySet()) {
                if (counter.get(p) >= 2) {
                    res += 1;
                }
            }
        }
        return res;
    }
    
    public List<Point> getPath(int[][] points, int[] route) {
        List<Point> visitPoints = new ArrayList<>();
        visitPoints.add(getPoint(route[0], points));
        
        for (int i = 1; i < route.length; i++) {
            Point des = getPoint(route[i], points);
            Point curPoint = visitPoints.get(visitPoints.size() - 1);
            int dr = des.r < curPoint.r ? -1 : 1;
            for (int j = 1; j <= Math.abs(des.r - curPoint.r); j++) {
                Point nxt = new Point(curPoint.r + dr * j, curPoint.c);
                visitPoints.add(nxt);
            }
            
            int dc = des.c < curPoint.c ? -1 : 1;
            for (int j = 1; j <= Math.abs(des.c - curPoint.c); j++) {
                Point nxt = new Point(des.r, curPoint.c + dc * j);
                visitPoints.add(nxt);
            }
        }
        return visitPoints;
    }
    
    public Point getPoint(int num, int[][] points) {
        return new Point(points[num - 1][0], points[num - 1][1]);
    }
}

class Point {
    public int r, c;
    
    public Point(int r, int c) {
        this.r = r;
        this.c = c;
    }
    
    @Override
    public String toString() {
        return "(" + r + ", " + c + ")";
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Point)) {
            return false;
        }
        Point p = (Point)o;
        return r == p.r && c == p.c;
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(r, c);
    }
}