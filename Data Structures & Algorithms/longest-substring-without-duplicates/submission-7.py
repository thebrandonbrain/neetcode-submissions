class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashed = {}
        left = 0
        maxed = 0

        for right in range(len(s)):
            if s[right] in hashed and hashed[s[right]] >= left:
                left = hashed[s[right]] + 1

            hashed[s[right]] = right
            maxed = max(maxed, right - left + 1)

        return maxed