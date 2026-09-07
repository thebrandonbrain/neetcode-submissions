class Solution:
    def minWindow(self, s: str, t: str) -> str:
        requirement = {}
        for char in t:
            if char not in requirement:
                requirement[char] = 1
            else:
                requirement[char] += 1
        required = len(requirement.keys())
        have = 0
        window = {}
        l, r = 0,0
        final = ""
        while r < len(s):
            if s[r] not in window:
                window[s[r]] = 1
            else:
                window[s[r]] += 1
            if s[r] in requirement and window[s[r]] == requirement[s[r]]:
                have += 1
                while have == required:
                    if not final or len(s[l:r+1]) < len(final):
                        final = s[l:r+1]
                    window[s[l]] -= 1
                    if s[l] in requirement and window[s[l]] < requirement[s[l]]:
                        have -= 1
                    l+= 1
            r+=1
        return final