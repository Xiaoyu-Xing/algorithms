// BFS, map, time O((r*c)^2) space O(r*c)
class Solution {
    public int cutOffTree(List<List<Integer>> forest) {
        List<int[]> trees = new ArrayList();
        for (int r = 0; r < forest.size(); r++) {
            for (int c = 0; c < forest.get(r).size(); c++) {
                int value = forest.get(r).get(c);
                if (value > 1) {
                    trees.add(new int[] {value, r, c});
                }
            }
        }
        Collections.sort(trees, (a, b) -> Integer.compare(a[0], b[0]));

        int ans = 0, sr = 0, sc = 0;
        for (int[] tree: trees) {
            int dis = dist(forest, sr, sc, tree[1], tree[2]);
            if (dis < 0) return -1;
            ans += dis;
            sr = tree[1];
            sc = tree[2];

        }
        return ans;
    }

    public int dist(List<List<Integer>> forest, int sr, int sc, int tr, int tc) {
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        int height = forest.size();
        int width = forest.get(0).size();
        Queue<int[]> queue = new LinkedList();
        // Queue includes the array of row#, column#, and distance to source
        queue.offer(new int[] {sr, sc, 0});
        boolean[][] seen = new boolean[height][width];
        seen[sr][sc] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            if (cur[0] == tr && cur[1] == tc) return cur[2];
            for (int di = 0; di < 4; di++) {
                int r = cur[0] + dr[di];
                int c = cur[1] + dc[di];
                if (0 <= r && r < height && 0 <= c && c < width && !seen[r][c] && forest.get(r).get(c) > 0) {
                    seen[r][c] = true;
                    queue.offer(new int[] {r, c, cur[2]+1});
                }
            }
        }
        return -1;
    }
}