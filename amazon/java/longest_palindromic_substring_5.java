// String, DP, O(n2) time and O(n2) space
class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2) return s;
        int[][] p = new int[len][len];
        for (int i = 0; i < len-1; i++) {
            p[i][i] = 1;
            p[i][i+1] = (s.charAt(i) == s.charAt(i+1)) ? 1 : 0;
        }
        p[len-1][len-1] = 1;
        // Draw a map of filling the number to figure out the loop
        // Build the map for 11 - 02, 22 - 12 - 04, 33 - 24 - 15 - 06, etc.
        for (int i = 1; i < len; i++) {
            for (int j = 1; j <= i && i + j < len; j++) {
                p[i-j][i+j] = (p[i-j+1][i+j-1] == 1 && s.charAt(i-j) == s.charAt(i+j)) ? 1 : 0;
            }
        }
        // Build the map for 12 - 03, 23 - 14 - 05, etc.
        for (int i = 1; i < len; i++) {
            for (int j = 1; j <= i && i + j + 1 < len; j++) {
                p[i-j][i+1+j] = (p[i-j+1][i+j] == 1 && s.charAt(i-j) == s.charAt(i+j+1)) ? 1 : 0;
            }
        }
        int maxLength = 0;
        int[] ans = {0, 0};
        for (int i = 0; i < len; i++) {
            for (int j = i; j < len; j++) {
                // Change the below < to <= would find the last match, < would find the first match, if ties exist.
                if (p[i][j] == 1 && maxLength <= j - i) {
                    maxLength = j - i;
                    ans = new int[] {i, j};
                }
            }
        }
        // System.out.println(Arrays.deepToString(p));
        // System.out.println(Arrays.toString(ans));
        return s.substring(ans[0], ans[1]+1);
    }
}


// Better solution, expanding around center
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            // +1 to get the total length of the substring, end and start both just pointers
            // change > to >= to get the later answer if ties exist
            if (len > end - start + 1) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private int expandAroundCenter(String s, int left, int right) {
        int L = left, R = right;
        while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
            L--;
            R++;
        }
        return R - L - 1;
    }
}