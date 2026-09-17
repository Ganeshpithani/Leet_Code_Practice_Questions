class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        rt=[]
        n=len(nums)
        for i in range(n-2):
            l=i+1
            r=n-1
            while l < r:
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    rt.append((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif s>0:
                    r-=1
                else:
                    l+=1
        lt=set(rt)
        return list(lt)
        