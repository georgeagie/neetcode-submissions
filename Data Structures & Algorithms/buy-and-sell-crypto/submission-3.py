class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = 0

        max_prof = 0

        for sell in range(len(prices)):
            if prices[buy] < prices[sell]: 
                max_prof = max(max_prof, prices[sell] - prices[buy])
            else:
                buy = sell

        return max_prof