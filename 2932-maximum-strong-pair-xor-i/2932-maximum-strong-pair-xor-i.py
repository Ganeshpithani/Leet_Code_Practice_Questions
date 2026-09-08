class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        r=float("-inf")
        for i in nums:
            for j in nums:
                if abs(i-j)<=min(i,j):
                    r=max(r,i^j)
        return r
        