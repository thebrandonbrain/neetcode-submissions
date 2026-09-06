class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_s = s.lower()
        lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        sentence = ''
        status = False
        for char in lowercase_s:
            if char in lis:
                sentence += char
        reverse_lowercase = sentence[::-1]
        if reverse_lowercase == sentence:
            status = True
        return status