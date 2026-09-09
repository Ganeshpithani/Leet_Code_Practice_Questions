class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while r>l:
            t=numbers[l]+numbers[r]
            if t==target:
                return [l+1,r+1]
            elif t>target:
                r-=1
            else:
                l+=1
