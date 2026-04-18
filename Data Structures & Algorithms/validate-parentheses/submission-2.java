class Solution {
    public boolean isValid(String s) {
        Stack<Character> parentheses = new Stack<>();
        HashMap<Character, Character> pairs = new HashMap<>();
        pairs.put(')', '(');
        pairs.put(']', '[');
        pairs.put('}', '{');
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (pairs.containsValue(c)) {
                parentheses.add(c);
            } else {
                if (parentheses.isEmpty()) return false;
                char match = parentheses.pop();
                if (pairs.get(c) != match) {
                    return false;
                }
            }
        }
        return parentheses.isEmpty();
    }
}
