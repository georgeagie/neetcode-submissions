class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int left = 0;
        int right = 0;
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                max = Math.max(prices[right] - prices[left], max);
                right++;
            } else {
                left = right;
                right++;
            }
        }
        return max;
    }
}
