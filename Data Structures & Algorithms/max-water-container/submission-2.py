class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_amt = 0
        while i < j:
            max_amt = max((min(heights[i], heights[j])*(j-i)), max_amt)
            if heights[i] <= heights[j]:
               i += 1
            elif heights[j] < heights[i]:
                j -= 1
            

        return max_amt
