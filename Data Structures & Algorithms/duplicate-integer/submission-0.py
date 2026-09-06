class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr = 0
        lis = {}
        while curr < len(nums):
            if nums[curr] not in lis:
                lis[nums[curr]] = curr
                curr += 1
            else:
                return True
        return False


