class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxed = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[i] < prices[j]:
                maxed = max(maxed, (prices[j] - prices[i]))
            else:
                i = j
            j += 1
        return maxed