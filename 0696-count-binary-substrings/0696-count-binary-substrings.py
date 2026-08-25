class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c=1
        r=[]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                r.append(c)
                c=1
        r.append(c)
        t=0
        for i in range(len(r)-1):
           t+=min(r[i],r[i+1])
        return t 