public class BSTNodeDistance {
	public class Node {
		Node left;
		Node right;
		int val;
		public Node (int v) {
			val = v;
			left = null;
			right = null;
		}
	}

	private Node insertNode(Node root, Node newNode) {
		if (root == null) {
			root = newNode;
			return root;
		}
		if (root.val < newNode.val) {
			if (root.right == null) {
				root.right = newNode;
				return root;
			} else {
				return insertNode(root.right, newNode);
			}

		} else if (root.val > newNode.val) {
			if (root.left == null) {
				root.left = newNode;
				return root;
			} else {
				return insertNode(root.left, newNode);
			}
		}
		return root;
	}
	
	public Node root;

	public BSTNodeDistance(int[] numbers) {
		root = null;
		for (int i = 0; i < numbers.length; i++) {
			Node newNode = new Node(numbers[i]);
			insertNode(root, newNode);
		}
	}
	
	private Node LCA(Node root, int a, int b) {
		// if a or b or both not in the BST, null or root may be returned
		if (root == null) {
			return null;
		}
		if (a > root.val && b > root.val) {
			return LCA(root.right, a, b);
		}
		if (a < root.val && b < root.val) {
			return LCA(root.left, a, b);
		}
		return root;
	}

	private int levelDifference(Node root, int x) {
		// if x not found, return -1, base case
		if (root == null) {
			return -1;
		} else if (root.val == x) {
			return 0;
		} else if (x > root.val) {
			int ans = levelDifference(root.right, x);
			return (ans == -1) ? -1 : ans + 1;
		} else if (x < root.val) {
			int ans = levelDifference(root.left, x);
			return (ans == -1) ? -1 : ans + 1;
		}
		return -1;
	}

	private int nodesDistance(Node root, int a, int b) {
		Node LCA = LCA(root, a, b);
		if (LCA == null) {
			return -1;
		}
		return levelDifference(LCA, a) + levelDifference(LCA, b);
	}
}

