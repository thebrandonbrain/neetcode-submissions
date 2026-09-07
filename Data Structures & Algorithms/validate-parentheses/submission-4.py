class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        closing = {')':'(', '}': '{', ']' : '['}
        for parentheses in s:
            if parentheses in closing:
                if lis and closing[parentheses] == lis[-1]:
                    lis.pop()
                else:
                    return False
            else:
                lis.append(parentheses)

            
                
        if not lis:
            return True
        return False