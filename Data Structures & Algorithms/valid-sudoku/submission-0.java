class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, HashSet<Character>> rows = new HashMap<>(); 
        HashMap<Integer, HashSet<Character>> cols = new HashMap<>(); 
        HashMap<String, HashSet<Character>> boxes = new HashMap<>(); 

        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board[row].length; col++) {
                if (board[row][col] == '.') continue;

                char c = board[row][col];
                String s = (row/3) + "," + (col/3);
                if (rows.computeIfAbsent(row, k -> new HashSet<>()).contains(c) ||
                    cols.computeIfAbsent(col, k -> new HashSet<>()).contains(c) ||
                    boxes.computeIfAbsent(s, k -> new HashSet<>()).contains(c)) {
                    return false;
                }
                rows.get(row).add(c);
                cols.get(col).add(c);
                boxes.get(s).add(c);
            }
        }
        return true;
    }
}
