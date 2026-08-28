class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        v=0
        l=0
        r=len(nums)-1
        while l<r:
            v+=int(str(nums[l])+str(nums[r]))
            l+=1
            r-=1
        if l==r:
            v+=nums[l]
        return v
        