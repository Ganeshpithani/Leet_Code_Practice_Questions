class Solution:
    def balancedStringSplit(self, s: str) -> int:
        b_c,l_c,r_c=0,0,0
        for i in range(len(s)):
            if s[i]=='L':
                l_c+=1
            else:
                r_c+=1
            if l_c==r_c:
                b_c+=1
        return b_c

        