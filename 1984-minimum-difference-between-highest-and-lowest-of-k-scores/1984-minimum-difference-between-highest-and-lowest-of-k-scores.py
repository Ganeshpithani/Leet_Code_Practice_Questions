class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        m=float("inf")
        r=k-1
        l=0
        while r<len(nums):
            m=min(m,nums[r]-nums[l])
            l+=1
            r+=1
        return m