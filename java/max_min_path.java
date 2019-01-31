public static int maximumMinimumPath(int[][] matrix) {

        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int n = matrix.length;
        int m = matrix[0].length;
        int[][] dp = new int[n][m];                             
        dp[0][0] = matrix[0][0];
        for (int i = 1; i < n; i++) {
            dp[i][0] = Math.min(dp[i - 1][0], matrix[i][0]); 
        }
        for (int i = 1; i < m; i++) {
            dp[0][i] = Math.min(dp[0][i - 1], matrix[0][i]);
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                // Current location can only be accessed from top and left,
                // choose max is because the worst case among these two points
                // then get the min of the current points and previous points
                // minMaxPath(i, j) = min(matrix(i, j), max(minMaxPath(i-1, j), minMaxPath(i, j-1)))
                dp[i][j] = Math.min(Math.max(dp[i - 1][j], dp[i][j - 1]),
                        matrix[i][j]);
            }
        }
        return dp[n - 1][m - 1];
    }

    public static void main(String[] args) {
        int[][] d = new int[][]{
                {8,4,3,5},
                {6,5,9,8},
                {7,2,3,6}
        } ;
        System.out.println(maximumMinimumPath(d)); // 5
    }
// can be optimized with space O(n)
int helper(int[][] matrix){
    int[] result = new int[matrix[0].length];
    result[0] = matrix[0][0];
    for(int i=1; i<matrix[0].length; i++){
        result[i] = Math.min(result[i-1], matrix[0][i]);
    }
    for(int i=1; i<matrix.length; i++){
        result[0] = Math.min(matrix[i][0], result[0]);
        for(int j=1; j<matrix[0].length; j++){
            result[j] = (result[j]<matrix[i][j] && result[j-1]<matrix[i][j])?Math.max(result[j-1], result[j]):matrix[i][j];
            }
        }
        return result[result.length-1];
}
// Or DFS:
 public class MaximumMinimumPath {
    private int min, max, row, col;
    public int maxMinPath(int[][] matrix) {
        row = matrix.length;
        col = matrix[0].length;
        min = Integer.MAX_VALUE;
        max = Integer.MIN_VALUE;
        dfsHelper(matrix, min, 0, 0);
     return max;
    }

    public void dfsHelper(int[][] matrix, int min, int i, int j ){                
        if (i >= row || j >= col) return;
        if (i == row - 1 && j == col - 1) {
            min = Math.min(min, matrix[i][j]);
            max = Math.max(max, min);
            return;
        }
        min = Math.min(min, matrix[i][j]);
        dfsHelper(matrix, min, i, j + 1);
        dfsHelper(matrix, min, i + 1, j);
    }
}