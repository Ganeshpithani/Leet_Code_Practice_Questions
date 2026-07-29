class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r=[]
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in s:
                r.append(i)
        return r
        