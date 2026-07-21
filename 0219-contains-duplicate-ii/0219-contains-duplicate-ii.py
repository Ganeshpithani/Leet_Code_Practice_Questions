class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i_m={}
        for i in range(len(nums)):
            if nums[i] in i_m:
                if i - i_m[nums[i]]<=k:
                    return True
            i_m[nums[i]]=i
        return False