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
        Point[] ans = new Point[k];
        if (points == null || points.length == 0) {
            return ans;
        }
        Queue<Point> distance = new PriorityQueue<>((a, b) -> {
            int diff = Double.compare(dist(b, origin), dist(a, origin));
            if (diff == 0) {
                diff = (a.x - b.x == 0) ? a.y - b.y : a.x - b.x;
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
            ans[i] = distance.poll();
        }
        return ans;
    }
    private double dist(Point a, Point b) {
        return Math.sqrt(Math.pow((a.x - b.x), 2) + Math.pow((a.y - b.y), 2));
    }
}