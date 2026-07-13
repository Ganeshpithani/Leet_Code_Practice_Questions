class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_c=0
        t_c=0
        if s=="":
            return True
        while t_c < len(t) and s_c < len(s):
            if s[s_c]==t[t_c]:
                s_c+=1
            t_c+=1
        if s_c==len(s):
            return True
        else:
            return False