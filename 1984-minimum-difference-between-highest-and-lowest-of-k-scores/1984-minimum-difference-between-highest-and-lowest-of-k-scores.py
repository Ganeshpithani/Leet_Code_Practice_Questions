class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        minimum=float('inf')
        for i in range(len(nums)-k+1):
            difference=nums[i+k-1]-nums[i]
            minimum=min(minimum,difference)
        return minimum