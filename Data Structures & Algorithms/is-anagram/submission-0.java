class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hm = new HashMap<>();
        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (hm.containsKey(c)) {
                hm.put(c, hm.get(c) + 1);
            } else {
                hm.put(c, 1);
            }
        }
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if (hm.containsKey(c)) {
                hm.put(c, hm.get(c) - 1);
            } else {
                return false;
            }
        }

        for (Integer count: hm.values()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
}
