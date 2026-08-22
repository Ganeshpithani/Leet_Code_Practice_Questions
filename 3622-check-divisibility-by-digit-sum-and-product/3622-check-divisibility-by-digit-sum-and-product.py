class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n==0:
            return False 
        temp=n
        s=0
        p=1
        while temp>0:
            d=temp%10
            s+=d
            p*=d
            temp//=10
        return n%(s+p)==0