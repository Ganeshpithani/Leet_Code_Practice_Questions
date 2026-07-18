class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s=min(nums)
        l=max(nums)
        rs=0
        num=1
        while num<=s:
            if s%num==0 and l%num==0:
                rs=num
            num+=1
        return rs
        
        