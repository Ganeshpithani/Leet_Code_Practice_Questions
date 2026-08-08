class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a_s=set(allowed)
        c=0
        for word in words:
            if all(ch in a_s for ch in word):
                c+=1
        return c