class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // if (s == null || s.length() == 0 || k == 0) return 0;
        HashMap<Character, Integer> d = new HashMap<Character, Integer>();
        int left = 0, result = 0;
        for (int i = 0; i < s.length(); i++) {
            d.put(s.charAt(i), i);
            if (d.size() > k) {
                int min = Collections.min(d.values());
                left = min + 1;
                d.remove(s.charAt(min));
            }
            result = Math.max(result, i - left + 1);
        }
        return result;
    }
}