class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        final = 0
        while r < len(s):

            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            most_common = max(count.values())

            target = r - l + 1 - most_common

            while target > k:
                count[s[l]] -= 1
                l += 1
                target = r - l + 1 - max(count.values())
            final = max(r-l+ 1, final)

            r += 1
        return final

