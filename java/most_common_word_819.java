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