class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        r=[0]*(l*2)
        for i in range(l*2):
            r[i]=nums[i%l]
        return r

        