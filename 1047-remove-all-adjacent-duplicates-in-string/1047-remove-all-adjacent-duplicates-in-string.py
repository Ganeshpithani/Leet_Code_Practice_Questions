class Solution:
    def removeDuplicates(self, s: str) -> str:
        r=[]
        for i in s:
            if r and r[-1]==i:
                r.pop()
            else:
                r.append(i)
        r="".join(r)
        return r
        