class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        st1=[]
        st2=[]
        for i in s:
            if i!='#':
                st1.append(i)
            elif st1:
                st1.pop()
        for j in t:
            if j!='#':
                st2.append(j)
            elif st2:
                st2.pop()
        return st1==st2
        