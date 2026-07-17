class Solution:
    def freqAlphabets(self, s: str) -> str:
        r=[]
        i=len(s)-1
        while i>=0:
            if s[i]=="#":
                num=int(s[i-2:i])
                r.append(chr(num+96))
                i-=3
            else:
                r.append(chr(int(s[i])+96))
                i-=1
        return "".join(r[::-1])

        