class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        max_amt = 0
        for i in range(len(heights)-1):
            max_amt = max((min(heights[i], heights[j])*(j-i)), max_amt)
            while i < j and heights[i] > heights[j]:
                j -= 1
                max_amt = max((min(heights[i], heights[j])*(j-i)), max_amt)
            
        return max_amt
