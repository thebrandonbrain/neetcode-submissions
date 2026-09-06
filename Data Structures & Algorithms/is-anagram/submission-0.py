class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lis1= {}
        lis2 = {}
        for letter in s:
            if letter not in lis1:
                lis1[letter] = 1
            else:
                lis1[letter] += 1
        for letter in t:
            if letter not in lis2:
                lis2[letter] = 1
            else:
                lis2[letter] += 1
        if lis1 == lis2:
            return True
        return False