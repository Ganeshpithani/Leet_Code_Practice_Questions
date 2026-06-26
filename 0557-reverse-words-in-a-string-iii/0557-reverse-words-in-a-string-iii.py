class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        r=[]
        for i in s:
            re=i[::-1]
            r.append(re)
        return " ".join(r)
        