class Solution {
    public boolean isPalindrome(String s) {
        String normal = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            c = Character.toLowerCase(c);
            if (Character.isLetter(c) || Character.isDigit(c)) normal += c;
        }
        int lastIndex = normal.length() - 1;
        if (normal.length() == 0 || normal.length() == 1) {
            return true;
        }
        for (int i = 0; i <= lastIndex / 2; i++) {
            if (normal.charAt(i) != normal.charAt(lastIndex - i)) return false;
        }
        return true;
    }
}
