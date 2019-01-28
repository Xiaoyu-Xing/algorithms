/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
// Priority queue, 
public class Solution {
    /*
     * @param points: a list of points
     * @param origin: a point
     * @param k: An integer
     * @return: the k closest points
     */
    public Point[] kClosest(Point[] points, Point origin, int k) {
        Point[] result = new Point[k];
        if (points == null || points.length == 0) {
            return result;
        }
        Queue<Point> distance = new PriorityQueue<>((a, b) -> {
            int diff = Double.compare(getDistance(b, origin), getDistance(a, origin));
            if (diff == 0) {
                diff = b.x - a.x;
            }
            if (diff == 0) {
                diff = b.y - a.y;
            }
            
            return diff;
        });
        
        for (Point point : points) {
            distance.add(point);
            if (distance.size() > k) {
                distance.poll();
            }
        }
        
        for (int i = k - 1; i >= 0; i--) {
            result[i] = distance.poll();
        }
        
        return result;
        
    }
    
    private double getDistance(Point a, Point b) {
        return Math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
    }
}