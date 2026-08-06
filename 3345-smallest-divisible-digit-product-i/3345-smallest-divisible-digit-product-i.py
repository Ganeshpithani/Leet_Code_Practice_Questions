class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p=1
            for i in str(n):
                p*=int(i)
            if p%t==0:
                return n
            n+=1        