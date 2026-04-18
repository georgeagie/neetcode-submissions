class Solution {
    public double myPow(double x, int n) {
        double result = 1;
        for (int i = 0; i < Math.abs(n); i++) {
            if (n > 0) result *= x;
            else result /= x;
        }
        return result;
    }
}
