public String mostCommonWord(String paragraph, String[] banned) {
    Map<String, Integer> count = new HashMap<>();
    Set<String> ban = new HashSet<>(Arrays.asList(banned));
    String[] words = paragraph.replaceAll("\\W+", " ").toLowerCase().split("\\s+");
    for (String w : words) {
        if (!ban.contains(w)){
            count.put(w, count.getOrDefault(w, 0) + 1);
        }
    }
    String ans = null;
    for (String w: count.keySet()) {
        if (ans == null || count.get(w) > count.get(ans)) {
            ans = w;
        }
    }
    return ans;
    // for the size of the same count of strings, could use another HashMap<Integer, Integer> countSame
    // for (Integer i : count.values()){
    //      countSame.put(i, countSame.getOrDefault(i, 0) + 1);
    // }
    //  
}

// If tie exists, return array, sort based on alphabet, return empty if occur max 1.
public String[] mostCommonWord(String paragraph, String[] banned) {
    if (paragraph == null || paragraph.length() == 0) return new String[]{};
    Map<String, Integer> count = new HashMap<>();
    Set<String> ban = new HashSet<>(Arrays.asList(banned));
    String[] words = paragraph.replaceAll("\\W+", " ").toLowerCase().split("\\s+");
    for (String w : words) {
        if (!ban.contains(w)){
            count.put(w, count.getOrDefault(w, 0) + 1);
        }
    }
    List<String> ansList = new ArrayList<String>();
    int max = 0;
    for (String w: count.keySet()) {
        int currCount = count.get(w);
        if (currCount > max) {
            max = currCount;
            ansList.clear();
            ansList.add(w);
        }
        else if (currCount == max) {
            ansList.add(w);
        }
    }
    if (max == 1) return new String[]{};
    Collections.sort(ansList, (a, b) -> {
      return a.compareTo(b);
    });
    return ansList.toArray(new String[ansList.size()]);
}