import java.util.HashMap;
import java.util.Map;

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

// If required to return all the substrings (or the # of substrings) to have exactly k distinct letters
class Solution {
    public String[] lengthOfLongestSubstringKDistinct(String s, int k) {
        // if (s == null || s.length() == 0 || k == 0) return 0;
        HashMap<Character, Integer> d = new HashMap<Character, Integer>();
        List<String> l = new ArrayList<String>();
        int left = 0, result = 0;
        for (int i = 0; i < s.length(); i++) {
            d.put(s.charAt(i), i);
            if (d.size == k) {
                l.add(s.substring(left, i + 1));
            }
            if (d.size() > k) {
                int min = Collections.min(d.values());
                left = min + 1;
                d.remove(s.charAt(min));
            }
            result = Math.max(result, i - left + 1);
        }
        return l.toArray(new String[l.size()]);
    }
}

// find exactly k distinct letters
public class CountKSubStr 
{ 
    // Function to count number of substrings 
    // with exactly k unique characters 
    int countkDist(String str, int k) 
    { 
        // Initialize result 
        int res = 0; 
  
        int n = str.length(); 
  
        // To store count of characters from 'a' to 'z' 
        int cnt[] = new int[26]; 
  
        // Consider all substrings beginning with 
        // str[i] 
        for (int i = 0; i < n; i++) 
        { 
            int dist_count = 0; 
  
            // Initializing count array with 0 
            Arrays.fill(cnt, 0); 
  
            // Consider all substrings between str[i..j] 
            for (int j=i; j<n; j++) 
            { 
                // If this is a new character for this 
                // substring, increment dist_count. 
                if (cnt[str.charAt(j) - 'a'] == 0) 
                    dist_count++; 
  
                // Increment count of current character 
                cnt[str.charAt(j) - 'a']++; 
  
                // If distinct character count becomes k, 
                // then increment result. 
                if (dist_count == k) 
                    res++; 
            } 
        } 
  
        return res; 
    } 
  
    // Driver Program 
    public static void main(String[] args) 
    { 
        CountKSubStr ob = new CountKSubStr(); 
        String ch = "abcbaa"; 
        int k = 3; 
        System.out.println("Total substrings with exactly " + 
                           k +    " distinct characters : "
                           + ob.countkDist(ch, k)); 
    } 
}