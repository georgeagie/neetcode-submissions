class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int c = matrix[0].length - 1;
        int check = 0;
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][c] == target) return true;
            else if (target < matrix[i][c]) {
                check = i;
                break;
            }
        }
        // int top = 0;
        // int bottom = matrix.length - 1;
        // while (top <= bottom) {
        //     int mid = (top + bottom) / 2;
        //     if (matrix[mid][c] == target) return true;
        //     else if (matrix[mid][c] > target) top = mid - 1;
        //     else bottom = mid + 1;
        // }
        // System.out.println(check);
        int l = 0;
        int r = c;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (matrix[check][mid] == target) return true;
            else if (matrix[check][mid] > target) r = mid - 1;
            else l = mid + 1;
        }
        return false;
    }
}
