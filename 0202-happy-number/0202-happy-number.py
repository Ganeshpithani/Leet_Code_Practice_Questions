class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n!=0 and n not in s:
            s.add(n)
            r=0
            while n>0:
                d=n%10
                r+=d*d
                n//=10
            n=r
        return n==1
        