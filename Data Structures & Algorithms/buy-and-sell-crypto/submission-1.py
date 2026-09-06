class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxed = 0
        for i in range(1, len(prices)):
            num = i
            while num > 0:
                num -= 1
                if prices[num] < prices[i]:
                    maxed = max(maxed, (prices[i] - prices[num]))
        return maxed