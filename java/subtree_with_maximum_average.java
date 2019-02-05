// Post order traversal and divide and conquer, O(n) time, O(logn) space for recursion
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
*/

public class Solution {
	double maxAvg = Integer.MIN_VALUE;
	TreeNode node = null;

	public TreeNode maxAvgSubtree (TreeNode root) {
		if (root == null) {
			return null;
		}
		recurseFind(root);
		return node;
	}
	public int[] recurseFind(TreeNode root) {
		if (root == null) {
			return new int[]{0, 0};
		}
		int[] left = recurseFind(root.left);
		int[] right = recurseFind(root.right);
		int currSum = left[0] + right[0] + root.val;
		int currCount = left[1] + right[1] + 1;
		double currAvg = (double)currSum / currCount;
		if (node == null || currAvg > maxAvg) {
			maxAvg = currAvg;
			node = root;
		}
		return new int[]{currSum, currCount};
	}
}


// Or define an ReturnType class
class ResultType {
    public int sum;
    public int count;
    public double avg;
    public TreeNode node;
    public ResultType(int sum, int count, double avg, TreeNode node) {
        this.sum = sum;
        this.count = count;
        this.node = node;
        this.avg = avg;
    }
}
public class Solution {
    /**
     * @param root the root of binary tree
     * @return the root of the maximum average of subtree
     */
    private double avger = Integer.MIN_VALUE;
    private TreeNode node = null;
    public TreeNode findSubtree2(TreeNode root) {
        // Write your code here
        if (root == null) {
            return null;
        }
        getSubtree(root);
        return node;
    }
    private ResultType getSubtree(TreeNode root) {
        if (root == null) {
            return new ResultType(0, 0, 0, null);
        }
        ResultType left = getSubtree(root.left);
        ResultType right = getSubtree(root.right);
        int sum = root.val + left.sum + right.sum;
        int num = 1 + left.count + right.count;
        if (avger < (double)sum / num) {
            avger = (double)sum / num;
            node = root;
        }
        return new ResultType(sum, num, (double)sum / num, root);
    }
}


//Or
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root the root of binary tree
     * @return the root of the maximum average of subtree
     */
    
    class ResultType {
        TreeNode node;
        int sum;
        int size;
        public ResultType(TreeNode node, int sum, int size) {
            this.node = node;
            this.sum = sum;
            this.size = size;
        }
    }
    
    private ResultType result = null;
    
    public TreeNode findSubtree2(TreeNode root) {
        // Write your code here
        if (root == null) {
            return null;
        }
        
        ResultType rootResult = helper(root);
        return result.node;
    }
    
    public ResultType helper(TreeNode root) {
        if (root == null) {
            return new ResultType(null, 0, 0);
        }
        
        ResultType leftResult = helper(root.left);
        ResultType rightResult = helper(root.right);
        
        ResultType currResult = new ResultType(
                    root, 
                    leftResult.sum + rightResult.sum + root.val, 
                    leftResult.size + rightResult.size + 1);
    
        if (result == null 
            || currResult.sum * result.size > result.sum * currResult.size) {
            result = currResult;
        }
        
        return currResult;
    }
    
}