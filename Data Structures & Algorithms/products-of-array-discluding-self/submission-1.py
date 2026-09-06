
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf = [0] * len(nums)
        pf[0] = 1
        sf = [0] * len(nums)
        sf[0] = 1
        for i in range(len(nums)):
            if i > 0:
                pf[i] = nums[i-1] * pf[i-1]
        reverse = nums[::-1]
        for i in range(len(nums)):
            if i > 0:
                sf[i] = reverse[i-1] * sf[i-1]
        suffix = sf[::-1]
        lis = [x * y for x, y in zip(pf, suffix)]
        return lis