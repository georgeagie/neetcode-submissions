class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String s: strs) {
            int[] characterCount = new int[26];
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                int letter = c - 'a';
                characterCount[letter]++;
            }
            String key = Arrays.toString(characterCount);
            if (map.get(key) == null) {
                map.put(key, new ArrayList<String>());
            }
            map.get(key).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
