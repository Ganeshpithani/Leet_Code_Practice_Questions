class Solution:
    def missingInteger(self, arr: List[int]) -> int:
        
        if not arr:
            return arr
        s=arr[0]
        i=1
        while i<len(arr) and arr[i]==arr[i-1]+1:
            s+=arr[i]
            i+=1
        while s in arr:
            s+=1
        return s

        