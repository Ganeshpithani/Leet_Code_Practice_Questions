class Solution:
    def detectCapitalUse(self, i: str) -> bool:
        if i.isupper():
            return True
        elif i.islower():
            return True
        elif i[0].isupper() and i[1:].islower():
            return True
        else:
            return False
            
