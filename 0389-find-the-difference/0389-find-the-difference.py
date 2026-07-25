class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r=0
        for i in s:
            r^=ord(i)
        for j in t:
            r^=ord(j)
        return chr(r)


        