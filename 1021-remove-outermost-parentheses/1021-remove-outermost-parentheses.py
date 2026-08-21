class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        open_count=0
        for ch in s:
            if ch=='(':
                if open_count>0:
                    res.append(ch)
                open_count+=1
            else:
                open_count-=1
                if open_count>0:
                    res.append(ch)
        return ''.join(res)